from tkinter import *

window = Tk()
#window.geometry("800x800")

frame = Frame(width=250, height=250, bg="green")
frame2 = Frame(width=250, height=250, bg="orange")

label1 = Label(master=frame, text="Hello, I'm inside a frame", bg="blue", fg="white")
label1.pack()
label2 = Label(master=frame, text="I'm  ALSO inside a frame", bg="red", fg="white")
label2.pack()

frame2.pack()
frame.pack()

window.mainloop()