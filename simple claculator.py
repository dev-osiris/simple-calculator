from tkinter import *
root = Tk()
root.title('Pro calculator')
e = Entry(root, width=40, border=5, font=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click(num):
    e.insert(END, num)


def clear():
    e.delete(0, END)


def add(entry):
    try:
        calculated_sum = 0
        clear()
        f = str(entry).split('+')
        for i in f:
            calculated_sum += int(i)
        return '=' + str(calculated_sum)
    except ValueError:
        clear()
        e.insert(END, "Try again (press 'clear' to clear the screen)")


button1 = Button(root, text='1', padx=60, font=40, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=60, font=40, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=60, font=40, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=60, font=40, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=60, font=40, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=60, font=40, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=60, font=40, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=60, font=40, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=60, font=40, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=60, font=40, pady=20, command=lambda: click(0))
button_plus = Button(root, text='+', padx=130, font=40, pady=20, command=lambda: click('+'))
button_clear = Button(root, text='clear', padx=47, font=40, pady=20, command=clear)
button_equal = Button(root, text='=', padx=131, font=40, pady=20, command=lambda: e.insert(END, add(e.get())))

# placement of buttons
button9.grid(row=1, column=0)
button8.grid(row=1, column=1)
button7.grid(row=1, column=2)

button6.grid(row=2, column=0)
button5.grid(row=2, column=1)
button4.grid(row=2, column=2)

button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_plus.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=5, column=0)

root.mainloop()
