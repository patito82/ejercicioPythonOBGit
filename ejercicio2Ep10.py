import tkinter
from tkinter import ttk
windows = tkinter.Tk()
windows.title("Lista elementos")
windows.geometry('400x400')
vp = tkinter.Frame(windows)
vp.grid(column=0, row=0, pady=(10, 10))
label = tkinter.Label(windows, text='Opciones')
label.grid(column=0, row=0)
lista = ttk.Combobox(windows,
    state='readonly', values=['op1', 'op2', 'op3'])
lista.current()
lista.grid(column=1, row=0)
windows.mainloop()
