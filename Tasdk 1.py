# importing tkinter

from tkinter import *
from tkinter import Tk

# Creating a window for tkinter.
window = Tk()
window.title("Student: Litha Kane")
window.geometry('700x400')
window.configure(background="#7C7FBC")

lb1 = Label(text="MSickID :", background="#7C7FBC", font="Bold")
lb1.grid(row=2, column=0)

fstNum = Entry(window)
fstNum.grid(row=2, column=4)

lb2 = Label(window, text="MDurationOfTreatment :", background="#7C7FBC", font="Bold")
lb2.grid(row=8, column=0)
lb2 = Entry(window)
lb2.grid(row=8, column=4)

lb3 = Label(window, text="MDoctorsID :", background="#7C7FBC", font="Bold")
lb3.grid(row=12, column=0)
lb2 = Entry(window)
lb2.grid(row=12, column=4)

# button
choose = IntVar()
Radiobutton(window,
            text="Cancer",
            padx=20, background="#7C7FBC",
            variable=choose,
            value=1).grid(row=14, column=0)

# another button
choose = IntVar()
Radiobutton(window,
            text="Influenza",
            padx=20, background="#7C7FBC",
            variable=choose,
            value=1).grid(row=16, column=0)


class Sick():
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def influenza(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


window.mainloop()
