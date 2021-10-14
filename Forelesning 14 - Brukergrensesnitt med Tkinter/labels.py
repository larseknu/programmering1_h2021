import tkinter as tk

window = tk.Tk()
window.title("Labels")

label = tk.Label(text="This is a label!", font=("Arial", 16))
label.pack()

label_2 = tk.Label(text="Label 2", font=("Arial", 16), bg="green", fg="white")
label_2.pack()

label_3 = tk.Label(text="Label 3 - 0", font=("Arial", 16), bg="blue", fg="white",
                   height=5, width=10)
label_3.pack()

window.mainloop()

#print("something")