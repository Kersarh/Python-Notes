from tkinter import *

def onMove(value):
    print('Значение шкалы: ', value)

root = Tk()
var = IntVar()
Scale(root, label='Scale', command=onMove,
      variable=var, from_=0, to=4, length=200, tickinterval=1,
      orient='horizontal').pack()
root.mainloop()