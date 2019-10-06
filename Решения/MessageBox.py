import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
messagebox.showinfo("info", "info message")

title = "title"
message = "message"

messagebox.askyesnocancel(title, message)
# Отображает окно с запросом, ДА, НЕТ, ОТМЕНА.

messagebox.askyesno(title, message)
# Отображает окно с запросом, ДА, НЕТ

messagebox.askretrycancel(title, message)
# Отображает окно с запросом, ПОВТОР ОТМЕНА

messagebox.askquestion(title, message)
# Отображает окно с запросом, ДА, НЕТ

messagebox.askokcancel(title, message)
# Отображает окно с запросом, OK, ОТМЕНА

#-----------------------------------------------------
# вывод через api windows
import ctypes
# Initialization
MBox = ctypes.windll.user32.MessageBoxW
# Show Message
MBox(None, 'Hello', 'Window title', 0)

##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No
##  6 : Cancel | Try Again | Continue
