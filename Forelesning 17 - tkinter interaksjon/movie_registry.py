import tkinter as tk
import tkinter_helper as tkh

def save_movie(movie_list, listbox_movies, ent_movie_title, ent_movie_year, ent_movie_duration):
    title = ent_movie_title.get()
    year = int(ent_movie_year.get())
    duration = int(ent_movie_duration.get())

    key = f"({year}) {title}"
    movie_list[key] = {'title': title, 'year': year, 'duration': duration}
    listbox_movies.insert(tk.END, key)


def item_selected(movie_list, listbox_movies, ent_movie_title, ent_movie_year, ent_movie_duration):
    cur_selection = listbox_movies.curselection()
    print(cur_selection)
    if cur_selection:
        global current_movie_title
        movie_id = listbox_movies.get(listbox_movies.curselection())
        movie = movie_list[movie_id]
        current_movie_title.set(movie['title'])
        #ent_movie_title.delete(0, tk.END)
        ent_movie_year.delete(0, tk.END)
        ent_movie_duration.delete(0, tk.END)
        #ent_movie_title.insert(0, movie['title'])
        ent_movie_year.insert(0, movie['year'])
        ent_movie_duration.insert(0, movie['duration'])


def clear_movie_entries(*entries):
    ent_movie_title.delete(0, tk.END)
    ent_movie_year.delete(0, tk.END)
    ent_movie_duration.delete(0, tk.END)

    for entry in entries:
        entry.delete(0, tk.END)


def delete_movie(movie_list, listbox_movies):
    cur_selection = listbox_movies.curselection()
    print(cur_selection)
    if cur_selection:
        movie_id = listbox_movies.get(cur_selection)
        movie_list.pop(movie_id)
        listbox_movies.delete(listbox_movies.curselection())
        clear_movie_entries()

        top = tk.Toplevel()
        top.attributes("-topmost", True)
        top.title('Movie Deleted')
        tk.Label(top, text=f"{movie_id} deleted").pack()
        tk.Button(top, text="OK", command=top.destroy).pack(padx=100)


movies = {'(2020) Soul': {'title': 'Soul', 'year': 2020, 'duration': 100},
          '(2021) Dune': {'title': 'Dune', 'year': 2021, 'duration': 156},}

window = tk.Tk()
window.title("Movie Register")

tkh.create_big_ui(32)

main_form = tk.Frame()
left_from = tk.Frame()

current_movie_title = tk.StringVar()
ent_movie_title = tk.Entry(main_form, textvariable=current_movie_title)
ent_movie_year = tk.Entry(main_form)
ent_movie_duration = tk.Entry(main_form)

lbl_movie_title = tk.Label(main_form, text="Title: ")
lbl_movie_year = tk.Label(main_form, text="Year: ")
lbl_movie_duration = tk.Label(main_form, text="Duration: ")

# Create a StringVar with a list of the movie names
movie_liststrings = tk.StringVar(value=list(movies.keys()))
listbox_movies = tk.Listbox(left_from, listvariable=movie_liststrings,
                            selectmode=tk.SINGLE)

# Create buttons
btn_save = tk.Button(main_form, text="Save", command=lambda: save_movie(movies, listbox_movies, ent_movie_title, ent_movie_year, ent_movie_duration))
btn_delete = tk.Button(left_from, text="Delete", command=lambda: delete_movie(movies, listbox_movies))

# Set up the input fields with labels in a frame
lbl_movie_title.grid(row=0, column=0, sticky=tk.E)
lbl_movie_year.grid(row=1, column=0, sticky=tk.E)
lbl_movie_duration.grid(row=2, column=0, sticky=tk.E)
ent_movie_title.grid(row=0, column=1)
ent_movie_year.grid(row=1, column=1)
ent_movie_duration.grid(row=2, column=1)
btn_save.grid(row=3, column=0, columnspan=2)

# Set up the left side frame
listbox_movies.pack()
btn_delete.pack()

# Put the frames in the window
left_from.pack(side=tk.LEFT)
main_form.pack(side=tk.LEFT, padx=20)

listbox_movies.bind('<<ListboxSelect>>', lambda event: item_selected(movies, listbox_movies, ent_movie_title, ent_movie_year, ent_movie_duration))

window.mainloop()
