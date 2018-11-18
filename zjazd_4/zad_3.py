import tkinter

def koszt_przejazdu():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    wynik.configure(text=(a/100)*b*c)

root = tkinter.Tk()

a_label = tkinter.Label(master=root, text="dystans")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="spalanie")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

c_label = tkinter.Label(master=root, text="cena paliwa")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()

wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()
wynik = tkinter.Label(master=root, text=" - ")
wynik.pack()

policz_button = tkinter.Button(master=root, text="Policz", command=koszt_przejazdu)
policz_button.pack()

root.title("Koszt przejazdu")
root.mainloop()

