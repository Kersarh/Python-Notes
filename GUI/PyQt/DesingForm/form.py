# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_QtApp(object):
    def setupUi(self, QtApp):
        if not QtApp.objectName():
            QtApp.setObjectName(u"QtApp")
        QtApp.resize(800, 600)
        self.action = QAction(QtApp)
        self.action.setObjectName(u"action")
        self.action_3 = QAction(QtApp)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(QtApp)
        self.centralwidget.setObjectName(u"centralwidget")
        QtApp.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QtApp)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        QtApp.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QtApp)
        self.statusbar.setObjectName(u"statusbar")
        QtApp.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)

        self.retranslateUi(QtApp)

        QMetaObject.connectSlotsByName(QtApp)
    # setupUi

    def retranslateUi(self, QtApp):
        QtApp.setWindowTitle(QCoreApplication.translate("QtApp", u"QtApp", None))
        self.action.setText(QCoreApplication.translate("QtApp", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_3.setText(QCoreApplication.translate("QtApp", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("QtApp", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("QtApp", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

