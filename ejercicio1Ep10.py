import tkinter
from tkinter import ttk,messagebox

def resetear():
    opf.set(None)


def valor1():
    tkinter.messagebox.showinfo(title='opcion 1', message='op1')


def valor2():
    tkinter.messagebox.showinfo(title='opcion 2', message='op2')


def valor3():
        tkinter.messagebox.showinfo(title='opcion 3', message='op3')


def valor4():
    tkinter.messagebox.showinfo(title='opcion 4', message='op4')



windows = tkinter.Tk()
windows.geometry('250x150')
opf = tkinter.IntVar()
op1 = tkinter.Radiobutton(windows, text='opcion 1',
                          variable=opf, value=1, command=valor1)
op1.grid()
op2 = tkinter.Radiobutton(windows, text='opcion 2',
                          variable=opf, value=2, command=valor2)
op2.grid()
op3 = tkinter.Radiobutton(windows, text='opcion 3',
                          variable=opf, value=3, command=valor3)
op3.grid()
op4 = tkinter.Radiobutton(windows, text='opcion 4',
                          variable=opf, value=4, command=valor4)
op4.grid()


reset = ttk.Button(windows, text="Reset", command=resetear)
reset.grid()
windows.mainloop()
