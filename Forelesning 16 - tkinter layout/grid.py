import tkinter as tk

window = tk.Tk()

window.rowconfigure([0, 1, 2], weight=1, minsize=250)
window.columnconfigure([0, 1], weight=1, minsize=250)

frame1 = tk.Frame(width=50, height=50, bg="green", relief=tk.RAISED, bd=10)
frame2 = tk.Frame(width=50, height=50, bg="blue", relief=tk.RAISED, bd=10)
frame3 = tk.Frame(width=50, height=50, bg="red", relief=tk.RAISED, bd=10)
frame4 = tk.Frame(width=50, height=50, bg="cyan", relief=tk.RAISED, bd=10)
frame5 = tk.Frame(width=50, height=50, bg="magenta", relief=tk.RAISED, bd=10)
frame6 = tk.Frame(width=50, height=50, bg="yellow", relief=tk.RAISED, bd=10)

tk.Label(master=frame1, text="Inside frame").pack(fill=tk.BOTH, expand=True)
tk.Label(master=frame2, text="Inside frame", bg="blue").pack()
tk.Label(master=frame3, text="Inside frame", bg="red").pack()
tk.Label(master=frame4, text="Inside frame", bg="cyan").pack()
tk.Label(master=frame5, text="Inside frame", bg="magenta").pack()
tk.Label(master=frame6, text="Inside frame", bg="yellow").pack()

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=1, column=0, sticky="s")
frame3.grid(row=2, column=0, sticky="se")
frame4.grid(row=1, column=1, sticky="n")
frame5.grid(row=1, column=1, sticky="s")
frame6.grid(row=2, column=1, sticky="new")

window.mainloop()
