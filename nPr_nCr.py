from tkinter import *
from tkinter.messagebox import *


def fact():
    n=int(num1.get())
    f=1
    for i in range(n):
        f=(i+1)*f
    ans_field.delete(0, 'end')
    ans_field.insert(0, f)


def fact(n):
    f=1
    for i in range(n):
        f=(i+1)*f
    return f

def npr():
    n = int(num1.get())
    r= int(num2.get())
    ans_field.delete(0, 'end')
    ans_field.insert(0, fact(n)/fact(n-r))

def ncr():
    n = int(num1.get())
    r= int(num2.get())
    ans_field.delete(0, 'end')
    ans_field.insert(0, fact(n)/(fact(n-r)*fact(r)))


main_window = Tk()
main_window.geometry('500x600')
Label(main_window, text="Enter the value of n").grid(row=0)
Label(main_window, text="Enter the value of r").grid(row=1)
Label(main_window, text="The Answer is:").grid(row=2)

num1 = Entry(main_window)
num2 = Entry(main_window)
ans_field = Entry(main_window)

num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
ans_field.grid(row=2, column=1)

Button(main_window, text='Quit', command=main_window.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main_window, text='nCr', command=ncr).grid(row=5, column=4, sticky=W, pady=4)
Button(main_window, text='nPr', command=npr).grid(row=5, column=1, sticky=W, pady=4)
Button(main_window, text='factorial', command=fact).grid(row=5, column=0, sticky=W, pady=4)

mainloop()
