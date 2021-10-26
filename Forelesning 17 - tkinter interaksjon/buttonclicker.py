import tkinter as tk
import tkinter_helper as tkih


def increment(number):
    #number = int(lbl_number['text'])
    #lbl_number["text"] = f"{number + 1}"
    number.set(number.get() + 1)


def we_changed(*args):
    print(f"We changed! New value: {number.get()}")
    print(args)


window = tk.Tk()

tkih.create_big_ui(32)

number = tk.IntVar(0)
number.trace("w", callback=we_changed)
lbl_number = tk.Label(textvariable=number)
#lbl_number = tk.Label(text=f"{0}")
lbl_number.pack()
#btn_increment = tk.Button(text="Click me!", command=increment)
btn_increment = tk.Button(text="Click me!", command=lambda: increment(number))
# Hvis vi ikke bruker "command" direkte på en button, kan vi bind'e museklikk til den (<Button-1> er venstre museklikk)
# btn_increment.bind("<Button-1>", func=increment)
btn_increment.pack()


window.mainloop()


