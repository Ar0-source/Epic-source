import tkinter as tk
from tkinter import scrolledtext
import requests

def send_to_website():
    user_input = entry.get()
    if not user_input:
        result_text.config(text="Please enter something")
        return

    url = "https://www.vinoland.net/manifest"  # Replace with your target URL
    params = {"input": user_input}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, response.text)
    except requests.RequestException as e:
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Input to Website")

# Create and place the entry widget
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the button
send_button = tk.Button(root, text="Send", command=send_to_website)
send_button.pack(pady=10)

# Create a scrolled text widget to display the result
result_text = scrolledtext.ScrolledText(root, width=50, height=10)
result_text.pack(pady=10)

# Run the application
root.mainloop()