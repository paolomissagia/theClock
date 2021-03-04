from tkinter import *
import time

root = Tk()
root.title('alarmTimer')
root.geometry('600x400')


def clock():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    day = time.strftime('%A')

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock)

    my_labelTwo.config(text=day)


def update():
    my_label.config(text='New Text')


my_label = Label(root, text="", font=("Helvetica", 48), fg="black", bg="white")
my_label.pack(pady=100)

my_labelTwo = Label(root, text='', font=("Helvetica", 24), fg="black", bg="white")
my_labelTwo.pack(pady=10)

clock()
root.mainloop()
