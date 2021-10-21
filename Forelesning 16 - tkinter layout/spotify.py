import tkinter as tk

window = tk.Tk()
window.minsize(1000, 800)

main_frame=tk.Frame(height=800, bg="yellow")

main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure([0, 2], minsize=200)
main_frame.columnconfigure(1, weight=5, minsize=600)

playlists = tk.Frame(master=main_frame, bg="blue")
main = tk.Frame(master=main_frame, width=250, height=250, bg="cyan")
friend_activity= tk.Frame(master=main_frame, bg="magenta")
play_bar = tk.Frame(width=250, height=100, bg="green")

tk.Label(master=main, text="TEST").place(rely=0.2, relx=0.5)
tk.Label(master=main, text="TESTING").place(x=150, y=150)

tk.Label(master=playlists, anchor="w", text="Home").pack(fill=tk.X)
tk.Label(master=playlists, anchor="w", text="Search").pack(fill=tk.X)
tk.Label(master=playlists, anchor="w", text="Your Library").pack(fill=tk.X)
tk.Label(master=playlists, anchor="w", text="Create playlist").pack(fill=tk.X)

playlists.grid(row=0, column=0, sticky="nswe")
main.grid(row=0, column=1, sticky="nsew")
friend_activity.grid(row=0, column=2, sticky="nsew")

main_frame.pack(fill=tk.BOTH, expand=True)
play_bar.pack(fill=tk.X)

testelements = tk.StringVar(value=["Something", "Or", "Other"])
listbox = tk.Listbox(master=friend_activity, listvariable=testelements)
listbox.pack()

listbox.insert(1, "TEST")

window.mainloop()