import tkinter


def sumuj():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik.configure(text=a + b)


root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Parametr a")
a_label.pack()
a_entry = tkinter.Entry(master=root)  # tworzy okienko
a_entry.pack()

b_label = tkinter.Label(master=root, text="Parametr a")
b_label.pack()
b_entry = tkinter.Entry(master=root)  # tworzy okienko
b_entry.pack()

wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()
wynik = tkinter.Label(master=root, text=" - ")
wynik.pack()

policz_button = tkinter.Button(master=root, text="Policz", command=sumuj)
policz_button.pack()
root.title("Sumator")  # nadaje tytuł

root.mainloop()  # pętla wychwytująca zachowania użytkownika
