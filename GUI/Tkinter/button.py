from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
    btn.config(text="Clicks {}".format(clicks))  # для первой кнопки


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(
    text="click",  # текст кнопки
    background="#555",  # фоновый цвет кнопки
    foreground="#ccc",  # цвет текста
    padx="20",  # отступ от границ до содержимого по горизонтали
    pady="8",  # отступ от границ до содержимого по вертикали
    font="16",  # высота шрифта
    command=click_button,  # действие
)
btn.pack(side=BOTTOM, fill=Y)

root.mainloop()
