import tkinter as tk

window = tk.Tk()

entry = tk.Entry(font=("Arial", 16), width=30)
entry.pack()

#insert - insert text
entry.insert(0, "Testing, testing...")
entry.insert(0, "<insert 2>")
entry.insert(15, "<insert 3>")

#delete - delete text
entry.delete(15, 25)

#entry.delete(0, tk.END)

#get
entry_content = entry.get()

window.mainloop()

print(entry_content)