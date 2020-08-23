#! F:\Projects\PyQt\venv\Scripts\python.exe
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from form import Ui_QtApp  # импорт сгенерированного файла


class QtApp(QMainWindow):
    def __init__(self):
        super(QtApp, self).__init__()
        self.ui = Ui_QtApp()
        self.ui.setupUi(self)
        


if __name__ == "__main__":
    app = QApplication([])
    widget = QtApp()
    widget.show()
    sys.exit(app.exec_())
