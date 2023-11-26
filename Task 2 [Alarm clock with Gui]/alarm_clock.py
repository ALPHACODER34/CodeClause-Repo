import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import time
import winsound

class CustomizableAlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        # Default values
        self.background_color = "#3b4371"
        self.window_width = 400
        self.window_height = 200

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.label_time = ttk.Label(root, textvariable=self.time_var, font=("Courier", 36, "bold"))
        self.label_time.grid(row=0, column=0, columnspan=2, pady=10)

        self.entry_time = ttk.Entry(root, font=("Courier", 14))
        self.entry_time.insert(0, "HH:MM:SS")
        self.entry_time.grid(row=1, column=0, columnspan=2, pady=10)

        self.btn_set_alarm = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.btn_set_alarm.grid(row=2, column=0, pady=10)

        self.btn_stop_alarm = ttk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.btn_stop_alarm.grid(row=2, column=1, pady=10)

        self.alarm_active = False
        self.update_time()

        # Configure window size and background color
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.configure(bg=self.background_color)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_var.set(current_time)
        self.root.after(1000, self.update_time)

        if self.alarm_active:
            if current_time == self.alarm_time:
                self.play_custom_alarm()
                self.alarm_active = False
                self.btn_set_alarm["state"] = tk.NORMAL
                self.btn_stop_alarm["state"] = tk.DISABLED
                self.label_time.grid_forget()
                self.entry_time.grid(row=0, column=0, columnspan=2, pady=10)

    def set_alarm(self):
        alarm_time_str = self.entry_time.get()
        try:
            self.alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").strftime("%H:%M:%S")
            self.time_var.set(self.alarm_time)
            self.entry_time.grid_forget()
            self.label_time.grid(row=0, column=0, columnspan=2, pady=10)
            self.alarm_active = True
            self.btn_set_alarm["state"] = tk.DISABLED
            self.btn_stop_alarm["state"] = tk.NORMAL
        except ValueError:
            pass

    def stop_alarm(self):
        self.alarm_active = False
        self.btn_set_alarm["state"] = tk.NORMAL
        self.btn_stop_alarm["state"] = tk.DISABLED

    def play_custom_alarm(self):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

# Create the GUI window
root = tk.Tk()
CustomizableAlarmClock(root)
root.mainloop()

