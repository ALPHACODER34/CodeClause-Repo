import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3

class VoiceAssistantGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voice Assistant")
        self.geometry("400x300")
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.setup_gui()

    def setup_gui(self):
        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(pady=10)

        self.listen_button = tk.Button(self, text="Listen", command=self.listen_command)
        self.listen_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.destroy)
        self.quit_button.pack(pady=5)

    def listen_command(self):
        try:
            with sr.Microphone() as source:
                self.output_text.insert(tk.END, "Listening...\n")
                self.update_idletasks()
                audio_data = self.recognizer.listen(source, timeout=5)
                self.output_text.insert(tk.END, "Recognizing...\n")
                self.update_idletasks()

            command = self.recognizer.recognize_google(audio_data)
            self.output_text.insert(tk.END, f"Command: {command}\n")
            self.execute_command(command)

        except sr.UnknownValueError:
            self.output_text.insert(tk.END, "Speech Recognition could not understand audio.\n")
        except sr.RequestError as e:
            self.output_text.insert(tk.END, f"Could not request results from Google Speech Recognition service; {e}\n")

    def execute_command(self, command):
        # Add your command execution logic here
        self.output_text.insert(tk.END, "Executing command...\n")
        self.update_idletasks()

        # For demonstration purposes, just echo the command
        self.output_text.insert(tk.END, f"Command Executed: {command}\n")
        self.update_idletasks()

        # Speak the result
        self.speak_text(f"Command Executed: {command}")

    def speak_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    app = VoiceAssistantGUI()
    app.mainloop()
