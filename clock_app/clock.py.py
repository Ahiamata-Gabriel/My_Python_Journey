from tkinter import *
from time import *


def update():
    time_str = strftime('%I:%M:%S %p')
    time_label.config(text=time_str)

    day_str = strftime('%A')
    day_label.config(text=day_str)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

time_label = Label(window, font=('Arial', 50), fg='#492859', bg='#e8bae7')
time_label.pack()

day_label = Label(window, font=('Roboto', 50, ),fg='#802939')
day_label.pack()

date_label = Label(window, font=("Rubik", 30), )
date_label.pack()

window.title('Mogul Inc')
icon = PhotoImage(file='gammy.png')
window.iconphoto(True, icon)

update()

window.mainloop()
