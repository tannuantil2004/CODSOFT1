import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Length must be at least 1")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result.set(password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid number: {e}")

generator = tk.Tk()
generator.title("Password Generator")
generator.configure(bg="#e0f7fa")  
canvas = tk.Canvas(generator, width=400, height=500, bg="#e0f7fa")
canvas.pack()
entry_label = tk.Label(generator, text="Enter password length:", bg="#e0f7fa")
canvas.create_window(200, 50, window=entry_label)
entry = tk.Entry(generator, width=20)
canvas.create_window(200, 100, window=entry)
result = tk.StringVar()
result_label = tk.Label(generator, textvariable=result, bg="#e0f7fa")
canvas.create_window(200, 200, window=result_label)
generate_button = tk.Button(generator, text="Generate Password", command=generate_password, bg="#00796b", fg="#ffffff", font=("Helvetica", 10, "bold"))
canvas.create_window(200, 150, window=generate_button)
generator.mainloop()
