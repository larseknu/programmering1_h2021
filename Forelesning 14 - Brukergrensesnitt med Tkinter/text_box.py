import tkinter as tk

window = tk.Tk()

text_box = tk.Text(font=("Areal", 16))
text_box.pack()

text_box.insert("1.0", "\n\n\n\n")

text_box.insert("1.0", "<insert 1>")
text_box.insert("3.0", "<insert 2>")
text_box.insert("3.3", "<insert 3>")

#text_box.delete("1.0", tk.END)
text_box.delete("1.0", "1.1000000000")

text_box_content = text_box.get("1.0", tk.END)

window.mainloop()

print(text_box_content)