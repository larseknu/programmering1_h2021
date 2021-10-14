import tkinter as tk

window = tk.Tk()
window.title("Buttons")

button = tk.Button(
    text="Button!",
    font=("Times New Roman", 20),
    bg="black",
    fg="white",
    height=2, width=10
)
button.pack()

label_2 = tk.Label(text="Label 2", font=("Arial", 16), bg="green", fg="white")
label_2.pack()

window.mainloop()