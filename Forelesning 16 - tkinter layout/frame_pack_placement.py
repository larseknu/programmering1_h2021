import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(width=250, height=250, bg="green", relief=tk.SUNKEN, bd=10)
frame2 = tk.Frame(width=250, height=250, bg="magenta", relief=tk.RAISED, bd=10)
frame3 = tk.Frame(width=250, height=250, bg="yellow", relief=tk.RIDGE, bd=20)

label1 = tk.Label(master=frame1, text="Hello, I'm inside a frame", bg="blue", fg="white")
label2 = tk.Label(master=frame1, text="I'm  ALSO inside a frame", bg="red", fg="white")
label3 = tk.Label(master=frame2, text="I'm inside another frame", bg="red", fg="white")

label1.pack(padx=20, pady=20, ipadx=50, ipady=50)
label2.pack()
label3.pack()

frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20, ipadx=50, ipady=200)
frame3.pack(side=tk.BOTTOM, fill=tk.X)
frame1.pack(fill=tk.BOTH, expand=True)

window.mainloop()