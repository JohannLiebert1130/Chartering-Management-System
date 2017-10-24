# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_signup(object):
    def setupUi(self, signup_dialog):
        signup_dialog.setObjectName("signup_dialog")
        signup_dialog.resize(420, 265)
        signup_dialog.setSizeGripEnabled(False)
        self.gridLayoutWidget = QtWidgets.QWidget(signup_dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 351, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.e_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.e_lineEdit.setObjectName("e_lineEdit")
        self.gridLayout.addWidget(self.e_lineEdit, 2, 1, 1, 1)
        self.usr_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.usr_lineEdit.setObjectName("usr_lineEdit")
        self.gridLayout.addWidget(self.usr_lineEdit, 0, 1, 1, 1)
        self.usr_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.usr_label.setEnabled(True)
        self.usr_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usr_label.setObjectName("usr_label")
        self.gridLayout.addWidget(self.usr_label, 0, 0, 1, 1)
        self.pw_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pw_lineEdit.setObjectName("pw_lineEdit")
        self.gridLayout.addWidget(self.pw_lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.signup_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.signup_btn.setObjectName("signup_btn")
        self.gridLayout.addWidget(self.signup_btn, 3, 1, 1, 1)

        self.retranslateUi(signup_dialog)
        QtCore.QMetaObject.connectSlotsByName(signup_dialog)

    def retranslateUi(self, signup_dialog):
        _translate = QtCore.QCoreApplication.translate
        signup_dialog.setWindowTitle(_translate("signup_dialog", "Sign Up"))
        self.usr_label.setText(_translate("signup_dialog", "User Name"))
        self.label_3.setText(_translate("signup_dialog", "Email"))
        self.label_2.setText(_translate("signup_dialog", "Password"))
        self.signup_btn.setText(_translate("signup_dialog", "Sign Up"))


class AppWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_signup()
        self.ui.setupUi(self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = AppWindow()
sys.exit(app.exec_())