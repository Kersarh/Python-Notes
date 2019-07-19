#! venv\Scripts\python.exe

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction
from PyQt5.QtCore import QSize
 
 
# Создаем класс для главного окна и наследуем его от  QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(400, 300))    # Размеры
        self.setWindowTitle("Hello world!")   # Заголовок

        central_widget = QWidget(self)          # Создаем центральный виджет
        self.setCentralWidget(central_widget)   # Устанавливаем
 
        grid_layout = QGridLayout(self)         # Создаём QGridLayout
        central_widget.setLayout(grid_layout)   # Устанавливаем в центральный виджет
 
        title = QLabel("text for QLabel", self)    # Создаём лейбл
        title.setAlignment(QtCore.Qt.AlignCenter)   # Устанавливаем позиционирование текста
        grid_layout.addWidget(title, 0, 0)          # и добавляем его в grid_layout

        exit_action = QAction("&Exit", self)    # Создаём Action exit
        exit_action.setShortcut('Ctrl+Q')       # Задаём для него хоткей
        exit_action.triggered.connect(qApp.quit) # Подключаем сигнал к слоту qApp.quit

        # Панель Меню
        file_menu = self.menuBar() # Создаем меню
        file_menu.addAction(exit_action) # добавляем в него exit_action
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow() # Создаем окно на основании класса MainWindow
    mw.show() # Отобразить окно
    sys.exit(app.exec())