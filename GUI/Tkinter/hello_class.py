# -*- coding: utf-8 -*-
from tkinter import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        # сохраняем ссылку на родительский виджет. Корневое окно Tk.
        self.parent = parent
        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

        ql = Label(self, text="Текст!!!")
        ql.place(x=10, y=50)  # или ql.pack()
        # Кнопки
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=10, y=10)

    def centerWindow(self):
        # Размер окна
        w = 250
        h = 150
        # Размер экрана
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == "__main__":
    main()
