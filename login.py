import sqlite3
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDesktopWidget, QAction, QDialog, QMainWindow

from main import Ui_MainWindow



class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.signup_btn = QtWidgets.QPushButton('Sign up')
        self.login_btn = QtWidgets.QPushButton('Login')
        self.pass_lineEdit = QtWidgets.QLineEdit()
        self.usr_lineEdit = QtWidgets.QLineEdit()
        self.pass_label = QtWidgets.QLabel('Password')
        self.usr_label = QtWidgets.QLabel('User Name')
        self.initUI()

    def initUI(self):
        grid = QtWidgets.QGridLayout()

        self.usr_label.setFixedHeight(20)
        grid.addWidget(self.usr_label, 0, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)

        self.pass_label.setFixedHeight(20)
        grid.addWidget(self.pass_label, 1, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.usr_lineEdit.setFixedHeight(25)
        grid.addWidget(self.usr_lineEdit, 0, 1, 1, 2, QtCore.Qt.AlignBottom)

        self.pass_lineEdit.setFixedHeight(25)
        grid.addWidget(self.pass_lineEdit, 1, 1, 1, 2, QtCore.Qt.AlignVCenter)

        self.login_btn.setFixedHeight(40)
        grid.addWidget(self.login_btn, 2, 1, 1, 2, QtCore.Qt.AlignTop)


        self.signup_btn.setFixedHeight(25)
        grid.addWidget(self.signup_btn, 0, 3, QtCore.Qt.AlignBottom)


        grid.setContentsMargins(30, 30, 30, 30)
        self.setLayout(grid)
        self.setFixedSize(420, 265)
        self.setWindowTitle('Login Window')
        self.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
