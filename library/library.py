# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Library_main(object):
    def setupUi(self, Library_main):
        Library_main.setObjectName("Library_main")
        Library_main.resize(1133, 570)
        self.centralwidget = QtWidgets.QWidget(Library_main)
        self.centralwidget.setObjectName("centralwidget")
        self.Day_To_Day_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Day_To_Day_btn.setGeometry(QtCore.QRect(20, 20, 80, 80))
        self.Day_To_Day_btn.setAutoFillBackground(False)
        self.Day_To_Day_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Day_To_Day_btn.setIcon(icon)
        self.Day_To_Day_btn.setIconSize(QtCore.QSize(75, 75))
        self.Day_To_Day_btn.setFlat(True)
        self.Day_To_Day_btn.setObjectName("Day_To_Day_btn")
        self.Books_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Books_btn.setGeometry(QtCore.QRect(20, 120, 80, 80))
        self.Books_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/bookshelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Books_btn.setIcon(icon1)
        self.Books_btn.setIconSize(QtCore.QSize(75, 75))
        self.Books_btn.setFlat(True)
        self.Books_btn.setObjectName("Books_btn")
        self.Users_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Users_btn.setGeometry(QtCore.QRect(20, 220, 80, 80))
        self.Users_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/profle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Users_btn.setIcon(icon2)
        self.Users_btn.setIconSize(QtCore.QSize(75, 75))
        self.Users_btn.setFlat(True)
        self.Users_btn.setObjectName("Users_btn")
        self.Settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Settings_btn.setGeometry(QtCore.QRect(20, 320, 80, 80))
        self.Settings_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings_btn.setIcon(icon3)
        self.Settings_btn.setIconSize(QtCore.QSize(75, 75))
        self.Settings_btn.setFlat(True)
        self.Settings_btn.setObjectName("Settings_btn")
        self.Themes_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Themes_btn.setGeometry(QtCore.QRect(20, 420, 80, 80))
        self.Themes_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/swatches.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Themes_btn.setIcon(icon4)
        self.Themes_btn.setIconSize(QtCore.QSize(75, 75))
        self.Themes_btn.setFlat(True)
        self.Themes_btn.setObjectName("Themes_btn")
        self.MainTabs_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabs_tabWidget.setGeometry(QtCore.QRect(120, 20, 1000, 480))
        self.MainTabs_tabWidget.setObjectName("MainTabs_tabWidget")
        self.Day_To_Day_tab = QtWidgets.QWidget()
        self.Day_To_Day_tab.setObjectName("Day_To_Day_tab")
        self.Day_To_Day_table = QtWidgets.QTableWidget(self.Day_To_Day_tab)
        self.Day_To_Day_table.setGeometry(QtCore.QRect(-1, 90, 1000, 390))
        self.Day_To_Day_table.setObjectName("Day_To_Day_table")
        self.Day_To_Day_table.setColumnCount(5)
        self.Day_To_Day_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Day_To_Day_table.setItem(0, 4, item)
        self.Day_To_Day_table.horizontalHeader().setCascadingSectionResizes(True)
        self.Day_To_Day_table.horizontalHeader().setDefaultSectionSize(100)
        self.Day_To_Day_table.horizontalHeader().setStretchLastSection(True)
        self.Day_To_Day_Name_input = QtWidgets.QLineEdit(self.Day_To_Day_tab)
        self.Day_To_Day_Name_input.setGeometry(QtCore.QRect(90, 30, 200, 30))
        self.Day_To_Day_Name_input.setObjectName("Day_To_Day_Name_input")
        self.Day_To_Day_Name_label = QtWidgets.QLabel(self.Day_To_Day_tab)
        self.Day_To_Day_Name_label.setGeometry(QtCore.QRect(20, 30, 70, 30))
        self.Day_To_Day_Name_label.setObjectName("Day_To_Day_Name_label")
        self.Day_To_Day_Type_select = QtWidgets.QComboBox(self.Day_To_Day_tab)
        self.Day_To_Day_Type_select.setGeometry(QtCore.QRect(400, 30, 130, 30))
        self.Day_To_Day_Type_select.setObjectName("Day_To_Day_Type_select")
        self.Day_To_Day_Type_select.addItem("")
        self.Day_To_Day_Type_select.addItem("")
        self.Day_To_Day_Days_select = QtWidgets.QComboBox(self.Day_To_Day_tab)
        self.Day_To_Day_Days_select.setGeometry(QtCore.QRect(640, 30, 130, 30))
        self.Day_To_Day_Days_select.setObjectName("Day_To_Day_Days_select")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Days_select.addItem("")
        self.Day_To_Day_Add_btn = QtWidgets.QPushButton(self.Day_To_Day_tab)
        self.Day_To_Day_Add_btn.setGeometry(QtCore.QRect(880, 30, 90, 30))
        self.Day_To_Day_Add_btn.setObjectName("Day_To_Day_Add_btn")
        self.Day_To_Day_Type_label = QtWidgets.QLabel(self.Day_To_Day_tab)
        self.Day_To_Day_Type_label.setGeometry(QtCore.QRect(330, 30, 70, 30))
        self.Day_To_Day_Type_label.setObjectName("Day_To_Day_Type_label")
        self.Day_To_Day_Days_label = QtWidgets.QLabel(self.Day_To_Day_tab)
        self.Day_To_Day_Days_label.setGeometry(QtCore.QRect(570, 30, 70, 30))
        self.Day_To_Day_Days_label.setObjectName("Day_To_Day_Days_label")
        self.MainTabs_tabWidget.addTab(self.Day_To_Day_tab, "")
        self.Books_tab = QtWidgets.QWidget()
        self.Books_tab.setObjectName("Books_tab")
        self.Books_tabWidget = QtWidgets.QTabWidget(self.Books_tab)
        self.Books_tabWidget.setGeometry(QtCore.QRect(-2, -1, 1001, 480))
        self.Books_tabWidget.setObjectName("Books_tabWidget")
        self.Books_Add_tab = QtWidgets.QWidget()
        self.Books_Add_tab.setObjectName("Books_Add_tab")
        self.Books_Add_Code_input = QtWidgets.QLineEdit(self.Books_Add_tab)
        self.Books_Add_Code_input.setGeometry(QtCore.QRect(680, 20, 291, 30))
        self.Books_Add_Code_input.setObjectName("Books_Add_Code_input")
        self.Books_Add_Description_input = QtWidgets.QPlainTextEdit(self.Books_Add_tab)
        self.Books_Add_Description_input.setGeometry(QtCore.QRect(20, 70, 451, 221))
        self.Books_Add_Description_input.setObjectName("Books_Add_Description_input")
        self.Books_Add_Title_input = QtWidgets.QLineEdit(self.Books_Add_tab)
        self.Books_Add_Title_input.setGeometry(QtCore.QRect(110, 20, 361, 30))
        self.Books_Add_Title_input.setObjectName("Books_Add_Title_input")
        self.Books_Add_Category_select = QtWidgets.QComboBox(self.Books_Add_tab)
        self.Books_Add_Category_select.setGeometry(QtCore.QRect(680, 70, 291, 30))
        self.Books_Add_Category_select.setObjectName("Books_Add_Category_select")
        self.Books_Add_Author_select = QtWidgets.QComboBox(self.Books_Add_tab)
        self.Books_Add_Author_select.setGeometry(QtCore.QRect(680, 120, 291, 30))
        self.Books_Add_Author_select.setObjectName("Books_Add_Author_select")
        self.Books_Add_Publisher_select = QtWidgets.QComboBox(self.Books_Add_tab)
        self.Books_Add_Publisher_select.setGeometry(QtCore.QRect(680, 170, 291, 30))
        self.Books_Add_Publisher_select.setObjectName("Books_Add_Publisher_select")
        self.Books_Add_Price_input = QtWidgets.QLineEdit(self.Books_Add_tab)
        self.Books_Add_Price_input.setGeometry(QtCore.QRect(680, 220, 131, 30))
        self.Books_Add_Price_input.setObjectName("Books_Add_Price_input")
        self.Books_Add_Save_btn = QtWidgets.QPushButton(self.Books_Add_tab)
        self.Books_Add_Save_btn.setGeometry(QtCore.QRect(433, 360, 131, 30))
        self.Books_Add_Save_btn.setObjectName("Books_Add_Save_btn")
        self.Books_Add_Title_label = QtWidgets.QLabel(self.Books_Add_tab)
        self.Books_Add_Title_label.setGeometry(QtCore.QRect(20, 20, 91, 30))
        self.Books_Add_Title_label.setObjectName("Books_Add_Title_label")
        self.Books_Add_Code_label = QtWidgets.QLabel(self.Books_Add_tab)
        self.Books_Add_Code_label.setGeometry(QtCore.QRect(560, 20, 121, 30))
        self.Books_Add_Code_label.setObjectName("Books_Add_Code_label")
        self.Books_Add_Price_label = QtWidgets.QLabel(self.Books_Add_tab)
        self.Books_Add_Price_label.setGeometry(QtCore.QRect(560, 220, 121, 30))
        self.Books_Add_Price_label.setObjectName("Books_Add_Price_label")
        self.Books_Add_Category_label = QtWidgets.QLabel(self.Books_Add_tab)
        self.Books_Add_Category_label.setGeometry(QtCore.QRect(560, 70, 121, 30))
        self.Books_Add_Category_label.setObjectName("Books_Add_Category_label")
        self.Books_Add_Author_label = QtWidgets.QLabel(self.Books_Add_tab)
        self.Books_Add_Author_label.setGeometry(QtCore.QRect(560, 120, 121, 30))
        self.Books_Add_Author_label.setObjectName("Books_Add_Author_label")
        self.Books_Add_Publisher_label = QtWidgets.QLabel(self.Books_Add_tab)
        self.Books_Add_Publisher_label.setGeometry(QtCore.QRect(560, 170, 121, 30))
        self.Books_Add_Publisher_label.setObjectName("Books_Add_Publisher_label")
        self.Books_tabWidget.addTab(self.Books_Add_tab, "")
        self.Books_Edit_tab = QtWidgets.QWidget()
        self.Books_Edit_tab.setObjectName("Books_Edit_tab")
        self.Books_Edit_Search_input = QtWidgets.QLineEdit(self.Books_Edit_tab)
        self.Books_Edit_Search_input.setGeometry(QtCore.QRect(270, 10, 291, 30))
        self.Books_Edit_Search_input.setObjectName("Books_Edit_Search_input")
        self.Books_Edit_Search_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Search_label.setGeometry(QtCore.QRect(180, 10, 91, 30))
        self.Books_Edit_Search_label.setObjectName("Books_Edit_Search_label")
        self.Books_Edit_Search_btn = QtWidgets.QPushButton(self.Books_Edit_tab)
        self.Books_Edit_Search_btn.setGeometry(QtCore.QRect(600, 10, 131, 30))
        self.Books_Edit_Search_btn.setObjectName("Books_Edit_Search_btn")
        self.line = QtWidgets.QFrame(self.Books_Edit_tab)
        self.line.setGeometry(QtCore.QRect(0, 40, 1001, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Books_Edit_Title_input = QtWidgets.QLineEdit(self.Books_Edit_tab)
        self.Books_Edit_Title_input.setGeometry(QtCore.QRect(110, 70, 361, 30))
        self.Books_Edit_Title_input.setObjectName("Books_Edit_Title_input")
        self.Books_Edit_Description_input = QtWidgets.QPlainTextEdit(self.Books_Edit_tab)
        self.Books_Edit_Description_input.setGeometry(QtCore.QRect(20, 120, 451, 221))
        self.Books_Edit_Description_input.setObjectName("Books_Edit_Description_input")
        self.Books_Edit_Code_input = QtWidgets.QLineEdit(self.Books_Edit_tab)
        self.Books_Edit_Code_input.setGeometry(QtCore.QRect(680, 70, 291, 30))
        self.Books_Edit_Code_input.setObjectName("Books_Edit_Code_input")
        self.Books_Edit_Code_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Code_label.setGeometry(QtCore.QRect(560, 70, 121, 30))
        self.Books_Edit_Code_label.setObjectName("Books_Edit_Code_label")
        self.Books_Edit_Publisher_select = QtWidgets.QComboBox(self.Books_Edit_tab)
        self.Books_Edit_Publisher_select.setGeometry(QtCore.QRect(680, 220, 291, 30))
        self.Books_Edit_Publisher_select.setObjectName("Books_Edit_Publisher_select")
        self.Books_Edit_Category_select = QtWidgets.QComboBox(self.Books_Edit_tab)
        self.Books_Edit_Category_select.setGeometry(QtCore.QRect(680, 120, 291, 30))
        self.Books_Edit_Category_select.setObjectName("Books_Edit_Category_select")
        self.Books_Edit_Author_select = QtWidgets.QComboBox(self.Books_Edit_tab)
        self.Books_Edit_Author_select.setGeometry(QtCore.QRect(680, 170, 291, 30))
        self.Books_Edit_Author_select.setObjectName("Books_Edit_Author_select")
        self.Books_Edit_Price_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Price_label.setGeometry(QtCore.QRect(560, 270, 121, 30))
        self.Books_Edit_Price_label.setObjectName("Books_Edit_Price_label")
        self.Books_Edit_Author_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Author_label.setGeometry(QtCore.QRect(560, 170, 121, 30))
        self.Books_Edit_Author_label.setObjectName("Books_Edit_Author_label")
        self.Books_Edit_Publisher_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Publisher_label.setGeometry(QtCore.QRect(560, 220, 121, 30))
        self.Books_Edit_Publisher_label.setObjectName("Books_Edit_Publisher_label")
        self.Books_Edit_Edit_btn = QtWidgets.QPushButton(self.Books_Edit_tab)
        self.Books_Edit_Edit_btn.setGeometry(QtCore.QRect(433, 360, 131, 30))
        self.Books_Edit_Edit_btn.setObjectName("Books_Edit_Edit_btn")
        self.Books_Edit_Category_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Category_label.setGeometry(QtCore.QRect(560, 120, 121, 30))
        self.Books_Edit_Category_label.setObjectName("Books_Edit_Category_label")
        self.Books_Edit_Price_input = QtWidgets.QLineEdit(self.Books_Edit_tab)
        self.Books_Edit_Price_input.setGeometry(QtCore.QRect(680, 270, 131, 30))
        self.Books_Edit_Price_input.setObjectName("Books_Edit_Price_input")
        self.Books_Edit_Title_label = QtWidgets.QLabel(self.Books_Edit_tab)
        self.Books_Edit_Title_label.setGeometry(QtCore.QRect(20, 70, 91, 30))
        self.Books_Edit_Title_label.setObjectName("Books_Edit_Title_label")
        self.Books_Edit_Delete_btn = QtWidgets.QPushButton(self.Books_Edit_tab)
        self.Books_Edit_Delete_btn.setGeometry(QtCore.QRect(20, 360, 131, 30))
        self.Books_Edit_Delete_btn.setObjectName("Books_Edit_Delete_btn")
        self.Books_tabWidget.addTab(self.Books_Edit_tab, "")
        self.MainTabs_tabWidget.addTab(self.Books_tab, "")
        self.Users_tab = QtWidgets.QWidget()
        self.Users_tab.setObjectName("Users_tab")
        self.Users_Add_box = QtWidgets.QGroupBox(self.Users_tab)
        self.Users_Add_box.setGeometry(QtCore.QRect(20, 20, 461, 440))
        self.Users_Add_box.setObjectName("Users_Add_box")
        self.Users_Add_Name_label = QtWidgets.QLabel(self.Users_Add_box)
        self.Users_Add_Name_label.setGeometry(QtCore.QRect(40, 80, 141, 30))
        self.Users_Add_Name_label.setObjectName("Users_Add_Name_label")
        self.Users_Add_Name_input = QtWidgets.QLineEdit(self.Users_Add_box)
        self.Users_Add_Name_input.setGeometry(QtCore.QRect(180, 80, 241, 30))
        self.Users_Add_Name_input.setObjectName("Users_Add_Name_input")
        self.Users_Add_Email_input = QtWidgets.QLineEdit(self.Users_Add_box)
        self.Users_Add_Email_input.setGeometry(QtCore.QRect(180, 130, 241, 30))
        self.Users_Add_Email_input.setObjectName("Users_Add_Email_input")
        self.Users_Add_Email_label = QtWidgets.QLabel(self.Users_Add_box)
        self.Users_Add_Email_label.setGeometry(QtCore.QRect(40, 130, 141, 30))
        self.Users_Add_Email_label.setObjectName("Users_Add_Email_label")
        self.Users_Add_Pass_input = QtWidgets.QLineEdit(self.Users_Add_box)
        self.Users_Add_Pass_input.setGeometry(QtCore.QRect(180, 180, 241, 30))
        self.Users_Add_Pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Users_Add_Pass_input.setObjectName("Users_Add_Pass_input")
        self.Users_Add_Pass_label = QtWidgets.QLabel(self.Users_Add_box)
        self.Users_Add_Pass_label.setGeometry(QtCore.QRect(40, 180, 141, 30))
        self.Users_Add_Pass_label.setObjectName("Users_Add_Pass_label")
        self.Users_Add_ConfirmPass_input = QtWidgets.QLineEdit(self.Users_Add_box)
        self.Users_Add_ConfirmPass_input.setGeometry(QtCore.QRect(180, 230, 241, 30))
        self.Users_Add_ConfirmPass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Users_Add_ConfirmPass_input.setObjectName("Users_Add_ConfirmPass_input")
        self.Users_Add_ConfirmPass_label = QtWidgets.QLabel(self.Users_Add_box)
        self.Users_Add_ConfirmPass_label.setGeometry(QtCore.QRect(40, 230, 141, 30))
        self.Users_Add_ConfirmPass_label.setObjectName("Users_Add_ConfirmPass_label")
        self.Users_Add_Add_btn = QtWidgets.QPushButton(self.Users_Add_box)
        self.Users_Add_Add_btn.setGeometry(QtCore.QRect(160, 310, 141, 30))
        self.Users_Add_Add_btn.setObjectName("Users_Add_Add_btn")
        self.Users_Edit_box = QtWidgets.QGroupBox(self.Users_tab)
        self.Users_Edit_box.setGeometry(QtCore.QRect(509, 20, 461, 440))
        self.Users_Edit_box.setObjectName("Users_Edit_box")
        self.Users_Edit_Login_Name_input = QtWidgets.QLineEdit(self.Users_Edit_box)
        self.Users_Edit_Login_Name_input.setGeometry(QtCore.QRect(180, 40, 241, 30))
        self.Users_Edit_Login_Name_input.setObjectName("Users_Edit_Login_Name_input")
        self.Users_Edit_Login_Pass_label = QtWidgets.QLabel(self.Users_Edit_box)
        self.Users_Edit_Login_Pass_label.setGeometry(QtCore.QRect(40, 90, 141, 30))
        self.Users_Edit_Login_Pass_label.setObjectName("Users_Edit_Login_Pass_label")
        self.Users_Edit_Login_Name_label = QtWidgets.QLabel(self.Users_Edit_box)
        self.Users_Edit_Login_Name_label.setGeometry(QtCore.QRect(40, 40, 141, 30))
        self.Users_Edit_Login_Name_label.setObjectName("Users_Edit_Login_Name_label")
        self.Users_Edit_Login_Pass_input = QtWidgets.QLineEdit(self.Users_Edit_box)
        self.Users_Edit_Login_Pass_input.setGeometry(QtCore.QRect(180, 90, 241, 30))
        self.Users_Edit_Login_Pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Users_Edit_Login_Pass_input.setObjectName("Users_Edit_Login_Pass_input")
        self.Users_Edit_Login_btn = QtWidgets.QPushButton(self.Users_Edit_box)
        self.Users_Edit_Login_btn.setGeometry(QtCore.QRect(160, 140, 141, 30))
        self.Users_Edit_Login_btn.setObjectName("Users_Edit_Login_btn")
        self.Users_Edit_Pass_input = QtWidgets.QLineEdit(self.Users_Edit_box)
        self.Users_Edit_Pass_input.setGeometry(QtCore.QRect(180, 300, 241, 30))
        self.Users_Edit_Pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Users_Edit_Pass_input.setObjectName("Users_Edit_Pass_input")
        self.Users_Edit_Pass_label = QtWidgets.QLabel(self.Users_Edit_box)
        self.Users_Edit_Pass_label.setGeometry(QtCore.QRect(40, 300, 141, 30))
        self.Users_Edit_Pass_label.setObjectName("Users_Edit_Pass_label")
        self.Users_Edit_ConfirmPass_label = QtWidgets.QLabel(self.Users_Edit_box)
        self.Users_Edit_ConfirmPass_label.setGeometry(QtCore.QRect(40, 350, 141, 30))
        self.Users_Edit_ConfirmPass_label.setObjectName("Users_Edit_ConfirmPass_label")
        self.Users_Edit_ConfirmPass_input = QtWidgets.QLineEdit(self.Users_Edit_box)
        self.Users_Edit_ConfirmPass_input.setGeometry(QtCore.QRect(180, 350, 241, 30))
        self.Users_Edit_ConfirmPass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Users_Edit_ConfirmPass_input.setObjectName("Users_Edit_ConfirmPass_input")
        self.Users_Edit_Name_input = QtWidgets.QLineEdit(self.Users_Edit_box)
        self.Users_Edit_Name_input.setGeometry(QtCore.QRect(180, 200, 241, 30))
        self.Users_Edit_Name_input.setObjectName("Users_Edit_Name_input")
        self.Users_Edit_Email_label = QtWidgets.QLabel(self.Users_Edit_box)
        self.Users_Edit_Email_label.setGeometry(QtCore.QRect(40, 250, 141, 30))
        self.Users_Edit_Email_label.setObjectName("Users_Edit_Email_label")
        self.Users_Edit_Email_input = QtWidgets.QLineEdit(self.Users_Edit_box)
        self.Users_Edit_Email_input.setGeometry(QtCore.QRect(180, 250, 241, 30))
        self.Users_Edit_Email_input.setObjectName("Users_Edit_Email_input")
        self.Users_Edit_Edit_btn = QtWidgets.QPushButton(self.Users_Edit_box)
        self.Users_Edit_Edit_btn.setGeometry(QtCore.QRect(160, 400, 141, 30))
        self.Users_Edit_Edit_btn.setObjectName("Users_Edit_Edit_btn")
        self.Users_Edit_Name_label = QtWidgets.QLabel(self.Users_Edit_box)
        self.Users_Edit_Name_label.setGeometry(QtCore.QRect(40, 200, 141, 30))
        self.Users_Edit_Name_label.setObjectName("Users_Edit_Name_label")
        self.line_2 = QtWidgets.QFrame(self.Users_Edit_box)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.MainTabs_tabWidget.addTab(self.Users_tab, "")
        self.Settings_tab = QtWidgets.QWidget()
        self.Settings_tab.setObjectName("Settings_tab")
        self.Settings_Categories_table = QtWidgets.QTableWidget(self.Settings_tab)
        self.Settings_Categories_table.setGeometry(QtCore.QRect(-1, 90, 320, 390))
        self.Settings_Categories_table.setObjectName("Settings_Categories_table")
        self.Settings_Categories_table.setColumnCount(1)
        self.Settings_Categories_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Categories_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Categories_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Categories_table.setItem(0, 0, item)
        self.Settings_Categories_table.horizontalHeader().setStretchLastSection(True)
        self.Settings_Categories_table.verticalHeader().setVisible(False)
        self.Settings_Authors_table = QtWidgets.QTableWidget(self.Settings_tab)
        self.Settings_Authors_table.setGeometry(QtCore.QRect(340, 90, 320, 390))
        self.Settings_Authors_table.setObjectName("Settings_Authors_table")
        self.Settings_Authors_table.setColumnCount(1)
        self.Settings_Authors_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Authors_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Authors_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Authors_table.setItem(0, 0, item)
        self.Settings_Authors_table.horizontalHeader().setStretchLastSection(True)
        self.Settings_Authors_table.verticalHeader().setVisible(False)
        self.Settings_Publishers_table = QtWidgets.QTableWidget(self.Settings_tab)
        self.Settings_Publishers_table.setGeometry(QtCore.QRect(680, 90, 320, 390))
        self.Settings_Publishers_table.setObjectName("Settings_Publishers_table")
        self.Settings_Publishers_table.setColumnCount(1)
        self.Settings_Publishers_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Publishers_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Publishers_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings_Publishers_table.setItem(0, 0, item)
        self.Settings_Publishers_table.horizontalHeader().setStretchLastSection(True)
        self.Settings_Publishers_table.verticalHeader().setVisible(False)
        self.Settings_New_Type_label = QtWidgets.QLabel(self.Settings_tab)
        self.Settings_New_Type_label.setGeometry(QtCore.QRect(40, 30, 90, 30))
        self.Settings_New_Type_label.setObjectName("Settings_New_Type_label")
        self.Settings_New_Type_select = QtWidgets.QComboBox(self.Settings_tab)
        self.Settings_New_Type_select.setGeometry(QtCore.QRect(130, 30, 150, 30))
        self.Settings_New_Type_select.setObjectName("Settings_New_Type_select")
        self.Settings_New_Type_select.addItem("")
        self.Settings_New_Type_select.addItem("")
        self.Settings_New_Type_select.addItem("")
        self.Settings_New_Name_input = QtWidgets.QLineEdit(self.Settings_tab)
        self.Settings_New_Name_input.setGeometry(QtCore.QRect(410, 30, 250, 30))
        self.Settings_New_Name_input.setObjectName("Settings_New_Name_input")
        self.Settings_New_Name_label = QtWidgets.QLabel(self.Settings_tab)
        self.Settings_New_Name_label.setGeometry(QtCore.QRect(320, 30, 90, 30))
        self.Settings_New_Name_label.setObjectName("Settings_New_Name_label")
        self.Settings_New_Create_btn = QtWidgets.QPushButton(self.Settings_tab)
        self.Settings_New_Create_btn.setGeometry(QtCore.QRect(700, 30, 90, 30))
        self.Settings_New_Create_btn.setObjectName("Settings_New_Create_btn")
        self.MainTabs_tabWidget.addTab(self.Settings_tab, "")
        self.Themes_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Themes_box.setGeometry(QtCore.QRect(770, 0, 370, 550))
        self.Themes_box.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.Themes_box.setTitle("")
        self.Themes_box.setObjectName("Themes_box")
        self.Themes_label = QtWidgets.QLabel(self.Themes_box)
        self.Themes_label.setGeometry(QtCore.QRect(40, 120, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Themes_label.setFont(font)
        self.Themes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Themes_label.setObjectName("Themes_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Themes_box)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 200, 271, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Themes_Buttons_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Themes_Buttons_grid.setContentsMargins(0, 0, 0, 0)
        self.Themes_Buttons_grid.setObjectName("Themes_Buttons_grid")
        self.Themes_3_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Themes_3_btn.sizePolicy().hasHeightForWidth())
        self.Themes_3_btn.setSizePolicy(sizePolicy)
        self.Themes_3_btn.setObjectName("Themes_3_btn")
        self.Themes_Buttons_grid.addWidget(self.Themes_3_btn, 1, 0, 1, 1)
        self.Themes_1_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Themes_1_btn.sizePolicy().hasHeightForWidth())
        self.Themes_1_btn.setSizePolicy(sizePolicy)
        self.Themes_1_btn.setObjectName("Themes_1_btn")
        self.Themes_Buttons_grid.addWidget(self.Themes_1_btn, 0, 0, 1, 1)
        self.Themes_2_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Themes_2_btn.sizePolicy().hasHeightForWidth())
        self.Themes_2_btn.setSizePolicy(sizePolicy)
        self.Themes_2_btn.setObjectName("Themes_2_btn")
        self.Themes_Buttons_grid.addWidget(self.Themes_2_btn, 0, 1, 1, 1)
        self.Themes_4_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Themes_4_btn.sizePolicy().hasHeightForWidth())
        self.Themes_4_btn.setSizePolicy(sizePolicy)
        self.Themes_4_btn.setObjectName("Themes_4_btn")
        self.Themes_Buttons_grid.addWidget(self.Themes_4_btn, 1, 1, 1, 1)
        Library_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Library_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 22))
        self.menubar.setObjectName("menubar")
        Library_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Library_main)
        self.statusbar.setObjectName("statusbar")
        Library_main.setStatusBar(self.statusbar)

        self.retranslateUi(Library_main)
        self.MainTabs_tabWidget.setCurrentIndex(0)
        self.Books_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Library_main)

    def retranslateUi(self, Library_main):
        _translate = QtCore.QCoreApplication.translate
        Library_main.setWindowTitle(_translate("Library_main", "Library"))
        item = self.Day_To_Day_table.verticalHeaderItem(0)
        item.setText(_translate("Library_main", "New Row"))
        item = self.Day_To_Day_table.horizontalHeaderItem(0)
        item.setText(_translate("Library_main", "Code"))
        item = self.Day_To_Day_table.horizontalHeaderItem(1)
        item.setText(_translate("Library_main", "Title"))
        item = self.Day_To_Day_table.horizontalHeaderItem(2)
        item.setText(_translate("Library_main", "Author"))
        item = self.Day_To_Day_table.horizontalHeaderItem(3)
        item.setText(_translate("Library_main", "Publisher"))
        item = self.Day_To_Day_table.horizontalHeaderItem(4)
        item.setText(_translate("Library_main", "Price"))
        __sortingEnabled = self.Day_To_Day_table.isSortingEnabled()
        self.Day_To_Day_table.setSortingEnabled(False)
        item = self.Day_To_Day_table.item(0, 0)
        item.setText(_translate("Library_main", "tr"))
        item = self.Day_To_Day_table.item(0, 1)
        item.setText(_translate("Library_main", "g"))
        item = self.Day_To_Day_table.item(0, 2)
        item.setText(_translate("Library_main", "iugg"))
        item = self.Day_To_Day_table.item(0, 3)
        item.setText(_translate("Library_main", "uyguyg"))
        item = self.Day_To_Day_table.item(0, 4)
        item.setText(_translate("Library_main", "456"))
        self.Day_To_Day_table.setSortingEnabled(__sortingEnabled)
        self.Day_To_Day_Name_input.setPlaceholderText(_translate("Library_main", "Enter Book Title"))
        self.Day_To_Day_Name_label.setText(_translate("Library_main", "Name"))
        self.Day_To_Day_Type_select.setItemText(0, _translate("Library_main", "Retrieve"))
        self.Day_To_Day_Type_select.setItemText(1, _translate("Library_main", "Rent"))
        self.Day_To_Day_Days_select.setItemText(0, _translate("Library_main", "1"))
        self.Day_To_Day_Days_select.setItemText(1, _translate("Library_main", "2"))
        self.Day_To_Day_Days_select.setItemText(2, _translate("Library_main", "3"))
        self.Day_To_Day_Days_select.setItemText(3, _translate("Library_main", "4"))
        self.Day_To_Day_Days_select.setItemText(4, _translate("Library_main", "5"))
        self.Day_To_Day_Days_select.setItemText(5, _translate("Library_main", "6"))
        self.Day_To_Day_Days_select.setItemText(6, _translate("Library_main", "7"))
        self.Day_To_Day_Days_select.setItemText(7, _translate("Library_main", "8"))
        self.Day_To_Day_Days_select.setItemText(8, _translate("Library_main", "9"))
        self.Day_To_Day_Days_select.setItemText(9, _translate("Library_main", "10"))
        self.Day_To_Day_Add_btn.setText(_translate("Library_main", "Add"))
        self.Day_To_Day_Type_label.setText(_translate("Library_main", "Type"))
        self.Day_To_Day_Days_label.setText(_translate("Library_main", "Days"))
        self.MainTabs_tabWidget.setTabText(self.MainTabs_tabWidget.indexOf(self.Day_To_Day_tab), _translate("Library_main", "Day To Day"))
        self.Books_Add_Save_btn.setText(_translate("Library_main", "Save"))
        self.Books_Add_Title_label.setText(_translate("Library_main", "Book Title"))
        self.Books_Add_Code_label.setText(_translate("Library_main", "Book Code"))
        self.Books_Add_Price_label.setText(_translate("Library_main", "Book Price"))
        self.Books_Add_Category_label.setText(_translate("Library_main", "Category"))
        self.Books_Add_Author_label.setText(_translate("Library_main", "Author"))
        self.Books_Add_Publisher_label.setText(_translate("Library_main", "Publisher"))
        self.Books_tabWidget.setTabText(self.Books_tabWidget.indexOf(self.Books_Add_tab), _translate("Library_main", "Add"))
        self.Books_Edit_Search_label.setText(_translate("Library_main", "Book Title"))
        self.Books_Edit_Search_btn.setText(_translate("Library_main", "Search"))
        self.Books_Edit_Code_label.setText(_translate("Library_main", "Book Code"))
        self.Books_Edit_Price_label.setText(_translate("Library_main", "Book Price"))
        self.Books_Edit_Author_label.setText(_translate("Library_main", "Author"))
        self.Books_Edit_Publisher_label.setText(_translate("Library_main", "Publisher"))
        self.Books_Edit_Edit_btn.setText(_translate("Library_main", "Edit Book"))
        self.Books_Edit_Category_label.setText(_translate("Library_main", "Category"))
        self.Books_Edit_Title_label.setText(_translate("Library_main", "Book Title"))
        self.Books_Edit_Delete_btn.setText(_translate("Library_main", "Delete"))
        self.Books_tabWidget.setTabText(self.Books_tabWidget.indexOf(self.Books_Edit_tab), _translate("Library_main", "Edit"))
        self.MainTabs_tabWidget.setTabText(self.MainTabs_tabWidget.indexOf(self.Books_tab), _translate("Library_main", "Books"))
        self.Users_Add_box.setTitle(_translate("Library_main", "Add New User"))
        self.Users_Add_Name_label.setText(_translate("Library_main", "User Name"))
        self.Users_Add_Email_label.setText(_translate("Library_main", "Email"))
        self.Users_Add_Pass_label.setText(_translate("Library_main", "Password"))
        self.Users_Add_ConfirmPass_label.setText(_translate("Library_main", "Confirm Password"))
        self.Users_Add_Add_btn.setText(_translate("Library_main", "Add User"))
        self.Users_Edit_box.setTitle(_translate("Library_main", "Edit User Information"))
        self.Users_Edit_Login_Pass_label.setText(_translate("Library_main", "Password"))
        self.Users_Edit_Login_Name_label.setText(_translate("Library_main", "User Name"))
        self.Users_Edit_Login_btn.setText(_translate("Library_main", "Login"))
        self.Users_Edit_Pass_label.setText(_translate("Library_main", "New Password"))
        self.Users_Edit_ConfirmPass_label.setText(_translate("Library_main", "Confirm Password"))
        self.Users_Edit_Email_label.setText(_translate("Library_main", "Email"))
        self.Users_Edit_Edit_btn.setText(_translate("Library_main", "Edit User"))
        self.Users_Edit_Name_label.setText(_translate("Library_main", "User Name"))
        self.MainTabs_tabWidget.setTabText(self.MainTabs_tabWidget.indexOf(self.Users_tab), _translate("Library_main", "Users"))
        item = self.Settings_Categories_table.verticalHeaderItem(0)
        item.setText(_translate("Library_main", "test"))
        item = self.Settings_Categories_table.horizontalHeaderItem(0)
        item.setText(_translate("Library_main", "Categories"))
        __sortingEnabled = self.Settings_Categories_table.isSortingEnabled()
        self.Settings_Categories_table.setSortingEnabled(False)
        item = self.Settings_Categories_table.item(0, 0)
        item.setText(_translate("Library_main", "Biography"))
        self.Settings_Categories_table.setSortingEnabled(__sortingEnabled)
        item = self.Settings_Authors_table.verticalHeaderItem(0)
        item.setText(_translate("Library_main", "test"))
        item = self.Settings_Authors_table.horizontalHeaderItem(0)
        item.setText(_translate("Library_main", "Authors"))
        __sortingEnabled = self.Settings_Authors_table.isSortingEnabled()
        self.Settings_Authors_table.setSortingEnabled(False)
        item = self.Settings_Authors_table.item(0, 0)
        item.setText(_translate("Library_main", "Jhon"))
        self.Settings_Authors_table.setSortingEnabled(__sortingEnabled)
        item = self.Settings_Publishers_table.verticalHeaderItem(0)
        item.setText(_translate("Library_main", "test"))
        item = self.Settings_Publishers_table.horizontalHeaderItem(0)
        item.setText(_translate("Library_main", "Publishers"))
        __sortingEnabled = self.Settings_Publishers_table.isSortingEnabled()
        self.Settings_Publishers_table.setSortingEnabled(False)
        item = self.Settings_Publishers_table.item(0, 0)
        item.setText(_translate("Library_main", "Penguin"))
        self.Settings_Publishers_table.setSortingEnabled(__sortingEnabled)
        self.Settings_New_Type_label.setText(_translate("Library_main", "Create New"))
        self.Settings_New_Type_select.setItemText(0, _translate("Library_main", "Category"))
        self.Settings_New_Type_select.setItemText(1, _translate("Library_main", "Author"))
        self.Settings_New_Type_select.setItemText(2, _translate("Library_main", "Publisher"))
        self.Settings_New_Name_label.setText(_translate("Library_main", "Name"))
        self.Settings_New_Create_btn.setText(_translate("Library_main", "Create"))
        self.MainTabs_tabWidget.setTabText(self.MainTabs_tabWidget.indexOf(self.Settings_tab), _translate("Library_main", "Settings"))
        self.Themes_label.setText(_translate("Library_main", "Apply New Theme"))
        self.Themes_3_btn.setText(_translate("Library_main", "Theme 3"))
        self.Themes_1_btn.setText(_translate("Library_main", "Theme 1"))
        self.Themes_2_btn.setText(_translate("Library_main", "Theme 2"))
        self.Themes_4_btn.setText(_translate("Library_main", "Theme 4"))
import icons_rc
