# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QmainWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTextEdit, QStyleFactory


def show_available_vessels(text):
    connection = sqlite3.connect('vesseldb.sqlite')
    result = connection.execute("SELECT * FROM Vessels WHERE state=0")
    for data in result:
        text.append("Vessel id:" + str(data[0]))

    connection.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 720)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)

        self.stackedWidget.setGeometry(QtCore.QRect(220, 20, 841, 651))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 841, 651))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setStyleSheet("margin-left:20px;margin-right:20px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.textEdit = QTextEdit()
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 797, 472))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        show_available_vessels(self.textEdit)
        self.scrollArea.setWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.rent_return_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rent_return_label.setFont(font)
        self.rent_return_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rent_return_label.setObjectName("rent_return_label")
        self.verticalLayout_2.addWidget(self.rent_return_label)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.number_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.number_label.setFont(font)
        self.number_label.setStyleSheet("margin-left:4px;")
        self.number_label.setObjectName("number_label")
        self.horizontalLayout_2.addWidget(self.number_label)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setStyleSheet("margin-right:4px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)

        self.rent_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rent_btn.sizePolicy().hasHeightForWidth())
        self.rent_btn.setSizePolicy(sizePolicy)
        self.rent_btn.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rent_btn.setFont(font)
        self.rent_btn.setStyleSheet("margin-top:4px;margin-bottom:4px;")
        self.rent_btn.setObjectName("rent_btn")

        self.rent_btn.clicked.connect(self.rent_check)
        self.horizontalLayout_3.addWidget(self.rent_btn)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)

        self.return_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_btn.sizePolicy().hasHeightForWidth())
        self.return_btn.setSizePolicy(sizePolicy)
        self.return_btn.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.return_btn.setFont(font)
        self.return_btn.setStyleSheet("margin-top:4px;margin-bottom:4px;")
        self.return_btn.setObjectName("return_btn")

        self.return_btn.clicked.connect(self.return_check)
        self.horizontalLayout_3.addWidget(self.return_btn)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 811, 641))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("margin-top:10px")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_2.setStyleSheet("margin-left:20px;margin-right:20px")
        self.textEdit_2.setObjectName("textEdit 2")
        self.textEdit_2.setFont(font)
        self.verticalLayout_3.addWidget(self.textEdit_2)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)

        self.vessel_show_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vessel_show_btn.sizePolicy().hasHeightForWidth())
        self.vessel_show_btn.setSizePolicy(sizePolicy)
        self.vessel_show_btn.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_show_btn.setFont(font)
        self.vessel_show_btn.setStyleSheet("")
        self.vessel_show_btn.setObjectName("vessel_show_btn")
        self.vessel_show_btn.clicked.connect(self.vessel_showall)
        self.horizontalLayout_6.addWidget(self.vessel_show_btn)

        self.add_new_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add_new_btn.setObjectName("add_new_btn")
        self.add_new_btn.clicked.connect(self.add_new_vessel)
        self.horizontalLayout_6.addWidget(self.add_new_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        self.number_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.number_lineEdit.setStyleSheet("")
        self.number_lineEdit.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.number_lineEdit)

        spacerItem6 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)

        self.state_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.state_lineEdit.setStyleSheet("")
        self.state_lineEdit.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.state_lineEdit)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.vessel_confirm_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.vessel_confirm_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_confirm_btn.setFont(font)
        self.vessel_confirm_btn.setStyleSheet("margin-left: 300px;margin-right: 300px;")
        self.vessel_confirm_btn.setObjectName("pushButton_2")

        self.vessel_confirm_btn.clicked.connect(self.change_vessel_info)
        self.verticalLayout_3.addWidget(self.vessel_confirm_btn)

        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 10, 811, 641))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("margin-top:10px")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)

        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textEdit_3.setStyleSheet("margin-left:20px;margin-right:20px")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_4.addWidget(self.textEdit_3)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(295, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)

        self.order_show_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_show_btn.sizePolicy().hasHeightForWidth())
        self.order_show_btn.setSizePolicy(sizePolicy)
        self.order_show_btn.setMinimumSize(QtCore.QSize(205, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.order_show_btn.setFont(font)
        self.order_show_btn.setStyleSheet("")
        self.order_show_btn.setObjectName("pushButton_3")

        self.order_show_btn.clicked.connect(self.order_showall)
        self.horizontalLayout_7.addWidget(self.order_show_btn)


        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_7.addWidget(self.checkBox)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)

        self.order_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.order_lineEdit.setStyleSheet("")
        self.order_lineEdit.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.order_lineEdit)

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.order_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.order_select_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.order_select_btn.setFont(font)
        self.order_select_btn.setStyleSheet("margin-left: 300px;margin-right: 300px;")
        self.order_select_btn.setObjectName("pushButton_4")

        self.order_select_btn.clicked.connect(self.order_select)
        self.verticalLayout_4.addWidget(self.order_select_btn)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 194, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)


        self.charter_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.charter_btn.sizePolicy().hasHeightForWidth())
        self.charter_btn.setSizePolicy(sizePolicy)
        self.charter_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.charter_btn.setFont(font)
        self.charter_btn.setObjectName("charter_btn")

        self.charter_btn.clicked.connect(self.charter_win)
        self.verticalLayout.addWidget(self.charter_btn)

        self.vessel_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vessel_btn.sizePolicy().hasHeightForWidth())
        self.vessel_btn.setSizePolicy(sizePolicy)
        self.vessel_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_btn.setFont(font)
        self.vessel_btn.setObjectName("vessel_btn")

        self.vessel_btn.clicked.connect(self.vessel_win)
        self.verticalLayout.addWidget(self.vessel_btn)

        self.order_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_btn.sizePolicy().hasHeightForWidth())
        self.order_btn.setSizePolicy(sizePolicy)
        self.order_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.order_btn.setFont(font)
        self.order_btn.setObjectName("order_btn")

        self.order_btn.clicked.connect(self.order_win)
        self.verticalLayout.addWidget(self.order_btn)

        spacerItem6 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.config_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.config_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.config_btn.setStyleSheet("margin-top:4px;margin-bottom:4px;")
        self.config_btn.setObjectName("config_btn")
        self.horizontalLayout.addWidget(self.config_btn)

        self.exit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.exit_btn.setStyleSheet("margin-top:4px;margin-bottom:4px;")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.horizontalLayout.addWidget(self.exit_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1075, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuUser = QtWidgets.QMenu(self.menuBar)
        self.menuUser.setObjectName("menuUser")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionName = QtWidgets.QAction(MainWindow)
        self.actionName.setObjectName("actionName")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuUser.addAction(self.actionName)
        self.menuUser.addAction(self.actionExit)
        self.menuBar.addAction(self.menuUser.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def charter_win(self):
        self.stackedWidget.setCurrentIndex(0)

    def vessel_win(self):
        self.stackedWidget.setCurrentIndex(1)

    def order_win(self):
        self.stackedWidget.setCurrentIndex(2)

    def rent_check(self):
        text = self.lineEdit.text()
        conn = sqlite3.connect('vesseldb.sqlite')
        cur = conn.cursor()
        try:
            cur.execute('SELECT state FROM Vessels WHERE id = ? ', (text,))
            vessel_state = cur.fetchone()[0]
            # print(type(vessel_state))
            if vessel_state == 0:
                cur.execute('''INSERT INTO Orders (state,bg_time,vessel_id) 
                        VALUES ( ? , datetime('now', 'localtime'),?)''', (0, text))
                cur.execute('''UPDATE Vessels SET state=1 WHERE id= ?''', (text,))
                self.statusbar.showMessage("rent successfully!")
                conn.commit()
                self.textEdit.clear()
                show_available_vessels(self.textEdit)
            if vessel_state == 1:
                self.statusbar.showMessage("The vessel is already used")
            if vessel_state == -1:
                self.statusbar.showMessage("The vessel is under maintenance")
        except:
            self.statusbar.showMessage("invalid number")

    def return_check(self):
        text = self.lineEdit.text()
        conn = sqlite3.connect('vesseldb.sqlite')
        cur = conn.cursor()
        try:
            cur.execute('SELECT state FROM Vessels WHERE id = ? ', (text,))
            vessel_state = cur.fetchone()[0]
            # print(vessel_state)
            if vessel_state == 1:
                cur.execute(
                    '''UPDATE Orders SET ed_time= datetime('now', 'localtime'),state = 1 WHERE state= 0 AND vessel_id= ?''',
                    (text,))
                cur.execute('''UPDATE Vessels SET state=0 WHERE id= ?''', (text,))
                self.statusbar.showMessage("Return the vessel successfully!")
                conn.commit()
                self.textEdit.clear()
                show_available_vessels(self.textEdit)
            if vessel_state == 0:
                self.statusbar.showMessage("The vessel is not used")
            if vessel_state == -1:
                self.statusbar.showMessage("The vessel is under maintenance")
        except:
            self.statusbar.showMessage("invalid number")

    def vessel_showall(self):
        conn = sqlite3.connect('vesseldb.sqlite')
        try:
            self.textEdit_2.clear()
            result = conn.execute('SELECT * FROM Vessels')
            for data in result:
                if data[1]==0:
                    self.textEdit_2.append("Vessel id:" + str(data[0])+"    State: Unused")
                if data[1]==1:
                    self.textEdit_2.append("Vessel id:" + str(data[0])+"    State: Occupied")
                if data[1]==-1:
                    self.textEdit_2.append("Vessel id:" + str(data[0])+"    State: Under Maintenance")
            conn.commit()
        except:
            self.statusbar.showMessage("Error occur")

    def add_new_vessel(self):
        conn = sqlite3.connect('vesseldb.sqlite')
        conn.execute("INSERT INTO Vessels(state) VALUES(?)", '0')
        conn.commit()
        self.vessel_showall()
        self.textEdit.clear()
        show_available_vessels(self.textEdit)


    def change_vessel_info(self):
        number=self.number_lineEdit.text()
        state=self.state_lineEdit.text()
        #print(type(state))
        if state!="0" and state!="1" and state!="-1":
            self.statusbar.showMessage("invalid state")
        else:
            if number and state:
                conn = sqlite3.connect('vesseldb.sqlite')
                cur = conn.cursor()
                try:
                    cur.execute('''UPDATE Vessels SET state=? WHERE id= ?''', (state,number))

                    self.statusbar.showMessage("update successfully!")
                    self.textEdit_2.clear()
                    result = conn.execute('SELECT * FROM Vessels')
                    for data in result:
                        if data[1] == 0:
                            self.textEdit_2.append("Vessel ID:" + str(data[0]) + "    State: Unused")
                        if data[1] == 1:
                            self.textEdit_2.append("Vessel ID:" + str(data[0]) + "    State: Occupied")
                        if data[1] == -1:
                            self.textEdit_2.append("Vessel ID:" + str(data[0]) + "    State: Under maintenance")
                    conn.commit()
                    self.textEdit.clear()
                    show_available_vessels(self.textEdit)
                except:
                    self.statusbar.showMessage("error")
            else:
                self.statusbar.showMessage("please input")

    def order_showall(self):
        flag=True
        conn = sqlite3.connect('vesseldb.sqlite')
        try:
            self.textEdit_3.clear()
            result = conn.execute('SELECT * FROM Orders')
            conn.commit()
            if self.checkBox.isChecked():
                self.textEdit_3.append("A.M.")
            for data in result:
                if self.checkBox.isChecked() and int(data[2][11:13])>=12 and flag:
                    self.textEdit_3.append("P.M.")
                    flag=False
                if data[1]==0:
                    self.textEdit_3.append("Order ID:" + str(data[0])+"    State: Uncompleted"+"    Begin Time:"+str(data[2])+"    End Time:"+str(data[3])+"    Vessel ID:"+str(data[4]))
                if data[1]==1:
                    self.textEdit_3.append("Order ID:" + str(data[0])+"    State: Completed"+"    Begin Time:"+str(data[2])+"    End Time:"+str(data[3])+"    Vessel ID:"+str(data[4]))
                if data[1]==-1:
                    self.textEdit_3.append("Vessel ID:" + str(data[0])+"    State: Canceled"+"    Begin Time:"+str(data[2])+"    End Time:"+str(data[3])+"    Vessel ID:"+str(data[4]))
        except:
            self.statusbar.showMessage("Error occur")

    def order_select(self):
        text=self.order_lineEdit.text()
        if text:
            conn = sqlite3.connect('vesseldb.sqlite')
            cur = conn.cursor()
            try:
                self.textEdit_3.clear()
                if self.comboBox.currentIndex()==0:
                    cur.execute('SELECT * FROM Orders WHERE id = ? ', (text,))
                    data = cur.fetchone()
                    if data[1]==0:
                        self.textEdit_3.append("Order ID:" + str(data[0])+"    State: Uncompleted"+"    Begin Time:"+str(data[2])+"    End Time:"+str(data[3])+"    Vessel ID:"+str(data[4]))
                    if data[1]==1:
                        self.textEdit_3.append("Order ID:" + str(data[0])+"    State: Completed"+"    Begin Time:"+str(data[2])+"    End Time:"+str(data[3])+"    Vessel ID:"+str(data[4]))
                    if data[1]==-1:
                        self.textEdit_3.append("Vessel ID:" + str(data[0])+"    State: Canceled"+"    Begin Time:"+str(data[2])+"    End Time:"+str(data[3])+"    Vessel ID:"+str(data[4]))

                elif self.comboBox.currentIndex()==1:
                    result=conn.execute('SELECT * FROM Orders WHERE state = ? ', (text,))
                    for data in result:
                        if data[1] == 0:
                            self.textEdit_3.append(
                                "Order ID:" + str(data[0]) + "    State: Uncompleted" + "    Begin Time:" + str(
                                    data[2]) + "    End Time:" + str(data[3]) + "    Vessel ID:" + str(data[4]))
                        if data[1] == 1:
                            self.textEdit_3.append(
                                "Order ID:" + str(data[0]) + "    State: Completed" + "    Begin Time:" + str(
                                    data[2]) + "    End Time:" + str(data[3]) + "    Vessel ID:" + str(data[4]))
                        if data[1] == -1:
                            self.textEdit_3.append(
                                "Vessel ID:" + str(data[0]) + "    State: Canceled" + "    Begin Time:" + str(
                                    data[2]) + "    End Time:" + str(data[3]) + "    Vessel ID:" + str(data[4]))
                else:
                    result = conn.execute('SELECT * FROM Orders WHERE vessel_id = ? ', (text,))
                    for data in result:
                        if data[1] == 0:
                            self.textEdit_3.append(
                                "Order ID:" + str(data[0]) + "    State: Uncompleted" + "    Begin Time:" + str(
                                    data[2]) + "    End Time:" + str(data[3]) + "    Vessel ID:" + str(data[4]))
                        if data[1] == 1:
                            self.textEdit_3.append(
                                "Order ID:" + str(data[0]) + "    State: Completed" + "    Begin Time:" + str(
                                    data[2]) + "    End Time:" + str(data[3]) + "    Vessel ID:" + str(data[4]))
                        if data[1] == -1:
                            self.textEdit_3.append(
                                "Vessel ID:" + str(data[0]) + "    State: Canceled" + "    Begin Time:" + str(
                                    data[2]) + "    End Time:" + str(data[3]) + "    Vessel ID:" + str(data[4]))
            except:
                self.statusbar.showMessage("Error occur")
        else:
            self.statusbar.showMessage("please input")


    def change_time_format(self):
        mytext = self.textEdit_3.toPlainText()
        print(mytext)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Available vessels"))
        self.rent_return_label.setText(_translate("MainWindow", "    Rent/Return"))
        self.number_label.setText(_translate("MainWindow", "Number"))
        self.rent_btn.setText(_translate("MainWindow", "Rent"))
        self.return_btn.setText(_translate("MainWindow", "Return"))
        self.label_6.setText(_translate("MainWindow", "Vessel Information"))
        self.vessel_show_btn.setText(_translate("MainWindow", "Show all"))
        self.add_new_btn.setText(_translate("MainWindow", "Add New"))
        self.label_3.setText(_translate("MainWindow", "Change Information"))
        self.label_4.setText(_translate("MainWindow", "Number"))
        self.label_5.setText(_translate("MainWindow", "State"))
        self.vessel_confirm_btn.setText(_translate("MainWindow", "Confirm Change"))
        self.label_7.setText(_translate("MainWindow", "Order Information"))
        self.order_show_btn.setText(_translate("MainWindow", "Show all"))
        self.checkBox.setText(_translate("MainWindow", "AM/PM"))
        self.label_8.setText(_translate("MainWindow", "Select Specific Order"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Order ID"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Order State"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vessel ID"))
        self.order_select_btn.setText(_translate("MainWindow", "Select"))
        self.charter_btn.setText(_translate("MainWindow", "Chartering Management"))
        self.vessel_btn.setText(_translate("MainWindow", "Vessel Information"))
        self.order_btn.setText(_translate("MainWindow", "Order Information"))
        self.config_btn.setText(_translate("MainWindow", "Config"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionName.setText(_translate("MainWindow", "Log out"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('GTK+'))
    Widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
