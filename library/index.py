from library import Ui_Library_main
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb

from pprint import pprint


class MainApp(QMainWindow, Ui_Library_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Open_Day_To_Day_tab(refresh=True)
        self.MainTabs_tabWidget.tabBar().setVisible(False)
        # self.Books_tabWidget.tabBar().setVisible(False)
        self.Toggle_Themes()
        self.currentId = None

    def Handle_Buttons(self):

        self.Day_To_Day_btn.clicked.connect(self.Open_Day_To_Day_tab)
        self.Books_btn.clicked.connect(self.Open_Books_tab)
        self.Users_btn.clicked.connect(self.Open_Users_tab)
        self.Settings_btn.clicked.connect(self.Open_Settings_tab)
        self.Themes_btn.clicked.connect(self.Toggle_Themes)

        self.Books_Add_Save_btn.clicked.connect(self.Add_Book)
        self.Books_Edit_Search_btn.clicked.connect(self.Search_Book)
        self.Books_Edit_Edit_btn.clicked.connect(self.Edit_Book)
        self.Books_Edit_Delete_btn.clicked.connect(self.Delete_book)

        self.Users_Add_Add_btn.clicked.connect(self.Add_User)
        self.Users_Edit_Login_btn.clicked.connect(self.Login)
        self.Users_Edit_Edit_btn.clicked.connect(self.Edit_User)

        self.Settings_New_Create_btn.clicked.connect(self.Add_Setting)

        self.Themes_1_btn.clicked.connect(self.Set_Theme_darkstyle)
        self.Themes_2_btn.clicked.connect(self.Set_Theme_breezedark)
        self.Themes_3_btn.clicked.connect(self.Set_Theme_breezelight)
        self.Themes_4_btn.clicked.connect(self.Set_Theme_Fusion)

    ####################################################################
    ################  Open Tabs  #######################################

    def Open_Day_To_Day_tab(self, refresh=False):
        self.currentId = None
        if self.MainTabs_tabWidget.currentIndex() != 0 or refresh:
            self.MainTabs_tabWidget.setCurrentIndex(0)
            self.fill_Table(self.Day_To_Day_table,
                            '''
                SELECT book_code, book_title, author_name, publisher_name, book_price
                FROM book
	                NATURAL JOIN author
                    NATURAL JOIN publisher
                            ''')

            data = self.db_Get_Data("SELECT book_title FROM book")
            completer = StringCompleter(data, self)
            self.Day_To_Day_Name_input.setCompleter(completer)

    def Open_Books_tab(self, refresh=False):
        self.currentId = None
        if self.MainTabs_tabWidget.currentIndex() != 1 or refresh:
            self.MainTabs_tabWidget.setCurrentIndex(1)
            self.Books_tabWidget.setCurrentIndex(0)

            self.fill_Select(self.Books_Add_Category_select,
                             "SELECT category_name FROM category")
            self.fill_Select(self.Books_Add_Author_select,
                             "SELECT author_name FROM author")
            self.fill_Select(self.Books_Add_Publisher_select,
                             "SELECT publisher_name FROM publisher")
            self.fill_Select(self.Books_Edit_Category_select,
                             "SELECT category_name FROM category")
            self.fill_Select(self.Books_Edit_Author_select,
                             "SELECT author_name FROM author")
            self.fill_Select(self.Books_Edit_Publisher_select,
                             "SELECT publisher_name FROM publisher")

            data = self.db_Get_Data("SELECT book_title FROM book")
            completer = StringCompleter(data, self)
            self.Books_Edit_Search_input.setCompleter(completer)

    def Open_Users_tab(self, refresh=False):
        self.currentId = None
        if self.MainTabs_tabWidget.currentIndex() != 2 or refresh:
            self.MainTabs_tabWidget.setCurrentIndex(2)

            self.User_Toggle_Edit()

            # Validation for passwords
            regex = QRegExp(".*")
            password_validator = QRegExpValidator(
                regex, self.Users_Add_Pass_input)
            self.Users_Add_Pass_input.setValidator(password_validator)

            # Confirm if username in db

            # Confirm if email in db

    def Open_Settings_tab(self, refresh=False):
        self.currentId = None
        if self.MainTabs_tabWidget.currentIndex() != 3 or refresh:
            self.MainTabs_tabWidget.setCurrentIndex(3)
            self.fill_Table(self.Settings_Categories_table,
                            "SELECT category_name FROM category")
            self.fill_Table(self.Settings_Authors_table,
                            "SELECT author_name FROM author")
            self.fill_Table(self.Settings_Publishers_table,
                            "SELECT publisher_name FROM publisher")

    def Toggle_Themes(self):
        if self.Themes_box.isHidden():
            self.Themes_box.show()
        else:
            self.Themes_box.hide()

    ####################################################################
    ################  Books  ###########################################

    def Add_Book(self):
        data = {}
        data['table'] = 'book'
        data['book_title'] = self.Books_Add_Title_input.text()
        data['book_description'] = self.Books_Add_Description_input.toPlainText()
        data['book_code'] = self.Books_Add_Code_input.text()
        data['category_id'] = self.db_Get_Id(
            'category', 'category_name', self.Books_Add_Category_select.currentText())
        data['author_id'] = self.db_Get_Id(
            'author', 'author_name', self.Books_Add_Author_select.currentText())
        data['publisher_id'] = self.db_Get_Id(
            'publisher', 'publisher_name', self.Books_Add_Publisher_select.currentText())
        data['book_price'] = self.Books_Add_Price_input.text()

        self.db_Add_Row(data)

        self.Clear_Book_Fields()

    def Search_Book(self):
        title = self.Books_Edit_Search_input.text()
        data = self.db_Get_Data(
            f"SELECT * FROM book WHERE (book_title = '{title}')", fetchone=True)

        self.currentId = data[0]

        self.Books_Edit_Title_input.setText(data[1])
        self.Books_Edit_Description_input.setPlainText(data[2])
        self.Books_Edit_Code_input.setText(data[3])
        self.Books_Edit_Category_select.setCurrentText(
            self.db_Get_Val_by_Id('category', 'category_name', data[4]))
        self.Books_Edit_Author_select.setCurrentText(
            self.db_Get_Val_by_Id('author', 'author_name', data[5]))
        self.Books_Edit_Publisher_select.setCurrentText(
            self.db_Get_Val_by_Id('publisher', 'publisher_name', data[6]))
        self.Books_Edit_Price_input.setText(str(data[7]))

    def Edit_Book(self):
        data = {}
        data['table'] = 'book'
        data['id'] = self.currentId
        data['book_title'] = self.Books_Edit_Title_input.text()
        data['book_description'] = self.Books_Edit_Description_input.toPlainText()
        data['book_code'] = self.Books_Edit_Code_input.text()
        data['category_id'] = self.db_Get_Id(
            'category', 'category_name', self.Books_Edit_Category_select.currentText())
        data['author_id'] = self.db_Get_Id(
            'author', 'author_name', self.Books_Edit_Author_select.currentText())
        data['publisher_id'] = self.db_Get_Id(
            'publisher', 'publisher_name', self.Books_Edit_Publisher_select.currentText())
        data['book_price'] = self.Books_Edit_Price_input.text()

        self.db_Edit_Row(data)

        self.Clear_Book_Fields()

    def Delete_book(self):
        data = {}
        data['table'] = 'book'
        data['id'] = self.currentId

        warning = QMessageBox.warning(
            self, 'Delete Book', 'Are you sure you want to delete this book', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.db_Delete_Row(data)
            self.Clear_Book_Fields()

    def Clear_Book_Fields(self):
        self.currentId = None
        self.Books_Edit_Search_input.clear()
        self.Books_Add_Title_input.clear()
        self.Books_Add_Description_input.clear()
        self.Books_Add_Code_input.clear()
        self.Books_Add_Category_select.setCurrentIndex(0)
        self.Books_Add_Author_select.setCurrentIndex(0)
        self.Books_Add_Publisher_select.setCurrentIndex(0)
        self.Books_Add_Price_input.clear()
        self.Books_Edit_Title_input.clear()
        self.Books_Edit_Description_input.clear()
        self.Books_Edit_Code_input.clear()
        self.Books_Edit_Category_select.setCurrentIndex(0)
        self.Books_Edit_Author_select.setCurrentIndex(0)
        self.Books_Edit_Publisher_select.setCurrentIndex(0)
        self.Books_Edit_Price_input.clear()

    ####################################################################
    ################  Users  ###########################################

    def Add_User(self):
        data = {}
        data['table'] = 'user'
        data['user_name'] = self.Users_Add_Name_input.text()
        data['user_email'] = self.Users_Add_Email_input.text()
        data['user_password'] = self.Users_Add_Pass_input.text()
        data['confirmPass'] = self.Users_Add_ConfirmPass_input.text()

        if data['confirmPass'] == data['user_password'] and data['user_name']:
            self.db_Add_Row(data)
            self.Clear_User_Fields()
        else:
            QMessageBox.warning(
                self, 'Add User', "Passwords don't match, please try again", QMessageBox.Ok)

    def Login(self):
        username = self.Users_Edit_Login_Name_input.text()
        password = self.Users_Edit_Login_Pass_input.text()

        self.currentId = self.db_Get_Id('user', 'user_name', username)

        if self.currentId:
            if password == self.db_Get_Val_by_Id('user', 'user_password', self.currentId):
                self.statusBar().showMessage('LogIn Successfull')
                self.Users_Edit_Name_input.setText(username)
                self.Users_Edit_Email_input.setText(
                    self.db_Get_Val_by_Id('user', 'user_email', self.currentId))
                self.User_Toggle_Edit(True)

            else:
                QMessageBox.warning(
                    self, 'LogIn', "Passwords don't match, please try again.", QMessageBox.Ok)
        else:
            QMessageBox.warning(
                self, 'LogIn', "There is no user registered with that name.", QMessageBox.Ok)

    def Edit_User(self):
        data = {}
        data['table'] = 'user'
        data['id'] = self.currentId
        data['user_name'] = self.Users_Edit_Name_input.text()
        data['user_email'] = self.Users_Edit_Email_input.text()

        if self.Users_Edit_Pass_input.text():
            data['user_password'] = self.Users_Edit_Pass_input.text()
            data['confirmPass'] = self.Users_Edit_ConfirmPass_input.text()

            if data['confirmPass'] != data['user_password']:
                QMessageBox.warning(
                    self, 'Add User', "Passwords don't match, please try again", QMessageBox.Ok)
                return

        self.db_Edit_Row(data)
        self.statusBar().showMessage('User Data Updated Successfully')
        self.Clear_User_Fields()

    def User_Toggle_Edit(self, edit=False):
        self.Users_Edit_Name_label.setEnabled(edit)
        self.Users_Edit_Email_label.setEnabled(edit)
        self.Users_Edit_Pass_label.setEnabled(edit)
        self.Users_Edit_ConfirmPass_label.setEnabled(edit)
        self.Users_Edit_Name_input.setEnabled(edit)
        self.Users_Edit_Email_input.setEnabled(edit)
        self.Users_Edit_Pass_input.setEnabled(edit)
        self.Users_Edit_ConfirmPass_input.setEnabled(edit)
        self.Users_Edit_Edit_btn.setEnabled(edit)

    def Clear_User_Fields(self):
        self.currentId = None
        self.User_Toggle_Edit()
        self.Users_Add_Name_input.clear()
        self.Users_Add_Email_input.clear()
        self.Users_Add_Pass_input.clear()
        self.Users_Add_ConfirmPass_input.clear()
        self.Users_Edit_Login_Name_input.clear()
        self.Users_Edit_Login_Pass_input.clear()
        self.Users_Edit_Name_input.clear()
        self.Users_Edit_Email_input.clear()
        self.Users_Edit_Pass_input.clear()
        self.Users_Edit_ConfirmPass_input.clear()

    ####################################################################
    ################  Settings  ########################################

    def Add_Setting(self):
        data = {}
        data["table"] = self.Settings_New_Type_select.currentText().lower()
        data[f"{data['table']}_name"] = self.Settings_New_Name_input.text()

        self.db_Add_Row(data)
        self.Settings_New_Name_input.clear()
        self.Open_Settings_tab(refresh=True)

    ####################################################################
    ################  Themes  ##########################################

    def Set_Theme_darkstyle(self):
        import themes.darkstyle as style
        self.setStyleSheet(style.load_stylesheet())

    def Set_Theme_breezedark(self):
        import themes.breezedark as style
        self.setStyleSheet(style.load_stylesheet())

    def Set_Theme_breezelight(self):
        import themes.breezelight as style
        self.setStyleSheet(style.load_stylesheet())

    def Set_Theme_Fusion(self):
        self.setStyle("Fusion")

    ####################################################################
    ################  --------  ########################################

    def fill_Table(self, table: QTableWidget, query, editable=False, delete=False):
        data = self.db_Get_Data(query)
        table.setRowCount(0)

        # if delete:
        #     table.setColumnCount(2)

        if data:
            for row, form in enumerate(data):
                table.insertRow(row)
                for column, item in enumerate(form):
                    cell = QTableWidgetItem(str(item))
                    if not editable:
                        cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    table.setItem(row, column, cell)

                # if delete:
                #     btn = QPushButton(table)
                #     btn.setText('X')
                #     table.setCellWidget(row, column +1, btn)

        # table.setSortingEnabled(True)

    def fill_Select(self, select: QComboBox, query):
        select.clear()
        data = self.db_Get_Data(query)
        for item in data:
            select.addItem(item[0])

    ####################################################################
    ################  Database  ########################################

    def db_Get_Id(self, table, column, value):
        query = f"SELECT {table}_id FROM {table} WHERE ({column} = '{value}')"
        a = self.db_Get_Data(query, fetchone=True)
        return a[0] if a else a

    def db_Get_Val_by_Id(self, table, column, id):
        query = f"SELECT {column} FROM {table} WHERE ({table}_id = {id})"
        a = self.db_Get_Data(query, fetchone=True)
        return a[0] if a else a

    def db_Get_Data(self, query='', fetchone=False):
        if query:
            try:
                db = MySQLdb.connect(
                    host="localhost", user="test", password="test", db="library")
                cur = db.cursor()

                cur.execute(query)
                if fetchone:
                    data = cur.fetchone()
                else:
                    data = cur.fetchall()

            except MySQLdb.Error as e:
                print('Error:', e)

            finally:
                cur.close()
                db.close()
                return data

    def db_Delete_Row(self, data: dict):
        if data['id']:
            try:
                db = MySQLdb.connect(host="localhost", user="test",
                                     password="test", db="library")
                cur = db.cursor()

                sql = f"DELETE FROM {data['table']} WHERE {data['table']}_id = {data['id']}"

                cur.execute(sql)
                db.commit()

            except MySQLdb.Error as e:
                print('Error:', e)

            finally:
                cur.close()
                db.close()
                self.statusBar().showMessage(
                    f"Deleted {data['table']} In '{data['table']}s'")

    def db_Edit_Row(self, data: dict):
        try:
            db = MySQLdb.connect(host="localhost", user="test",
                                 password="test", db="library")
            cur = db.cursor()

            cur.execute(f"DESCRIBE {data['table']}")
            allowed_keys = set(row[0] for row in cur.fetchall())

            keys = allowed_keys.intersection(data)

            if len(keys) == 0:
                raise MySQLdb.Error

            values = list((f"{key}='{value}'" for key,
                           value in data.items() if key in allowed_keys))
            sql = f"UPDATE {data['table']} SET { ','.join(values)} WHERE ({data['table']}_id = {data['id']})"

            cur.execute(sql)
            db.commit()

        except MySQLdb.Error as e:
            print('Error:', e)

        finally:
            cur.close()
            db.close()
            self.statusBar().showMessage(
                f"Edited {data['table']} In '{data['table']}s'")

    def db_Add_Row(self, data: dict):
        try:
            db = MySQLdb.connect(host="localhost", user="test",
                                 password="test", db="library")
            cur = db.cursor()

            cur.execute(f"DESCRIBE {data['table']}")
            allowed_keys = set(row[0] for row in cur.fetchall())

            keys = allowed_keys.intersection(data)

            if len(keys) == 0:
                raise MySQLdb.Error

            columns = ", ".join(keys)
            values_template = ", ".join(["%s"] * len(keys))

            sql = f"INSERT INTO {data['table']} ({columns}) VALUES ({values_template})"
            values = tuple(data[key] for key in keys)

            cur.execute(sql, values)
            db.commit()

        except MySQLdb.Error as e:
            print('Error:', e)

        finally:
            cur.close()
            db.close()
            self.statusBar().showMessage(
                f"New {data['table']} Added To '{data['table']}s'")


class StringCompleter(QCompleter):
    ConcatenationRole = Qt.UserRole + 1

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.create_model(data)
        self.setCaseSensitivity(Qt.CaseInsensitive)

    def create_model(self, data):

        model = QStandardItemModel(self)
        self.addItems(model, data)
        self.setModel(model)

    def addItems(self, parent: QStandardItemModel, elements, t=""):
        for text in elements:
            if text[0]:
                item = QStandardItem(text[0])
                data = text[0]
                item.setData(data, self.ConcatenationRole)
                parent.appendRow(item)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
