import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(width=250, height=250, bg="magenta")
frame2 = tk.Frame(width=250, height=250, bg="blue")

frame1.pack()
frame2.pack(fill=tk.X)

label1 = tk.Label(text="Sith's deal in absolutes")
label2 = tk.Label(master=frame2, text="Sith's deal in absolutes too")
label3 = tk.Label(master=frame1, text="Relativity is nice")
label4 = tk.Label(master=frame2, text="Relativity is nice")

label1.place(x=100, y=100)
label2.place(x=100, y=100)
label3.place(relx=0.2, rely=0.8)
label4.place(relx=0.2, rely=0.8)

window.mainloop()