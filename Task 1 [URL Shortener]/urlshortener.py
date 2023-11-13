import tkinter as tk
import pyshorteners

root = tk.Tk()
root.title("URL Shortener Link")
root.geometry("800x300")

# Defining colors
bg_color = "#e9d362"  # Background color
text_color = "#fff"  # Text color
button_color = "#333333"  # Button color

#theme colors
root.configure(bg=bg_color)
root.option_add('*background', bg_color)
root.option_add('*foreground', text_color)
root.option_add('*Button.background', button_color)

#input field for the user URL
url_entry = tk.Entry(root)
url_entry.pack(pady=10) 

#Rext field to display the short URL
short_url_textfield = tk.Text(root, height=1, width=50)
short_url_textfield.pack(pady=10)

#Button to generate short URL
shorten_button = tk.Button(root, text="Generate Short URL", command=lambda: shorten_url(url_entry, short_url_textfield))
shorten_button.pack(pady=10)

#Button to copy short URL 
copy_button = tk.Button(root, text="Copy Short URL", command=lambda: copy_short_url(short_url_textfield))
copy_button.pack(pady=10)

#Sisplay message
message_label = tk.Label(root, text="")
message_label.pack(pady=10)

#Function to shorten the URL
def shorten_url(url_entry, short_url_textfield):
    url = url_entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)

    short_url_textfield.delete("1.0", "end")
    short_url_textfield.insert("end", short_url)

#To copy the short URL 
def copy_short_url(short_url_textfield):
    root.clipboard_clear()
    root.clipboard_append(short_url_textfield.get("1.0", "end"))

    message_label.config(text="Short URL copied !")


root.mainloop()
