import tkinter as tk

root = tk.Tk()

message = tk.Label(root, text="Click the button")
message.pack(pady=16)

def on_click():
    message.config(text="Button clicked!")
button = tk.Button(
    root, text="Rent Camera", command=on_click
)
button.pack(pady=8)
root.mainloop()