import sys
from PyQt5.QtWinExtras import QtWin
from PyQt5 import QtCore, QtWidgets, QtGui
from add_dialog import Add_Ui_Dialog
from password_manager_backend import PasswordManager
from password_prompt_dialog import Password_Ui_Dialog
from setup_dialog import Setup_Ui_Dialog
from cryptography.fernet import InvalidToken
from remove_dialog import Remove_Ui_Dialog

class Ui_MainWindow():
    def setupUi(self):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(557, 492)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 40, 161, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 256, 441))
        self.textBrowser.setObjectName("textBrowser")
        
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Password Manager")
        
        self.addButton.setText("Add")
        self.removeButton.setText("Remove")
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addButton.clicked.connect(self.add_button_clicked)
        self.removeButton.clicked.connect(self.remove_button_clicked)
    
    def reload_entries(self):
        self.textBrowser.clear()
        self.load_entries()

    def load_entries(self):
        lines = backend.list_accounts(self.universal_password)
        if lines:                                                           # if there are any accounts
            for line in lines:                                              # for every line in the text file containing the accounts
                convertdict = eval(line)                                    # evaluate (convert) the line in string type to python dictionary
                for credential, value in convertdict.items():               # for every key (credential) and value (account information) pair in the account dictionary
                    self.textBrowser.append(f"{credential}: {value}")       # append the credential and value to the text browser widget
                self.textBrowser.append("\n")

    def setup_promot(self):
        self.setup_dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)    # these arguments remove the question mark from the dialog window
        self.password_setup_ui = Setup_Ui_Dialog()
        self.password_setup_ui.setupUi(self.setup_dialog)
        self.setup_dialog.show()
        self.password_setup_ui.setupPushButton.clicked.connect(self.setup_button_clicked)

    def setup_button_clicked(self):
        password_1 = self.password_setup_ui.passwordLineEdit.text()                     # getting the user entered text content from the two text edit widgets
        password_2 = self.password_setup_ui.confirmPasswordLineEdit.text()
        if password_1 == password_2:                                                    # checking if the passwords match (so that the user is sure that they've typed the right passsword)
            self.universal_password = password_1                                        # set the universal password instance variable to the first text edit widget (it doesn't mstter which widget the text is from as they contain the same password), this variable is used throughout the class to pass to encryption related functions
            backend.generate_files()                                                    
            backend.generate_salt()
            backend.encrypt(self.universal_password)
            MainWindow.show()                                                           # user has successfully setup the password manager so the main window is shown and
            self.setup_dialog.close()                                                   # the setup dialog window is closed
        else:
            self.password_setup_ui.label_2.show()                                       # if the passwords do not match, a label is shown saying the passwords don't match

    
    def password_prompt(self):
        self.password_dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)     # these arguments remove the question mark from the dialog window
        self.password_ui = Password_Ui_Dialog()
        self.password_ui.setupUi(self.password_dialog)
        self.password_dialog.show()
        self.password_ui.enterPasswordPushButton.clicked.connect(self.enter_password_button_clicked)
    
    def enter_password_button_clicked(self):
        self.universal_password = self.password_ui.passwordLineEdit.text()
        try:                                                    
            backend.generate_salt()                                                     # this is still called so that the PasswordManager class can access the salt when it needs to encrypt/decrypt (it justs reads the salt file, it does not actually generate a new salt if there already is one)
            backend.check_correct_password(self.universal_password)
        except InvalidToken:
            self.password_ui.label.show()                                               # if invalid token is raised, show a label which says that the password is incorrect
        else:
            MainWindow.show()                                                           # if there is no invalid token exception, the user is validated and the main window is shown and the
            self.password_dialog.close()                                                # login window is closed
            self.load_entries()                                                         # loading all the stored accounts to text browser widget

    def add_button_clicked(self):
        self.add_dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.add_ui = Add_Ui_Dialog()
        self.add_ui.setupUi(self.add_dialog)
        self.add_ui.addEntryButton.clicked.connect(self.add_entry_button_clicked)
        self.add_ui.peekPassButton.clicked.connect(self.add_peek_pass_button_clicked)
        self.add_ui.generatePassButton.clicked.connect(self.generate_pass_button_clicked)
        self.add_peek_pass_bool = False
        self.add_dialog.setModal(True)                                                              # sets the modality to True, this means the add account dialog is focused and the user cannot interact with the main window until this dialog is finished or closed
        self.add_dialog.show()
        self.add_dialog.exec_()
    
    def add_entry_button_clicked(self):
        self.account = self.add_ui.accountLineEdit.text()
        self.username = self.add_ui.usernameLineEdit.text()
        self.password = self.add_ui.passwordLineEdit.text()
        if not self.account or not self.username or not self.password:
            self.add_ui.label_2.show()
        else:
            backend.add_account(self.account, self.username, self.password, self.universal_password)
            self.reload_entries()
            self.add_dialog.close()
    
    def remove_button_clicked(self):
        self.remove_dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.remove_ui = Remove_Ui_Dialog()
        self.remove_ui.setupUi(self.remove_dialog)
        self.remove_dialog.setModal(True)
        accounts = backend.load_QCombobox_items(self.universal_password)
        if accounts:
            for value in accounts.values():
                self.remove_ui.comboBox.addItem(value)
            self.remove_ui.removeEntryButton.clicked.connect(self.remove_entry_button_clicked)
        self.remove_dialog.show()
        self.remove_dialog.exec_()
    
    def remove_entry_button_clicked(self):
        index = self.remove_ui.comboBox.currentIndex()
        backend.remove_account(self.universal_password, index)
        self.reload_entries()
        self.remove_dialog.close()
    
    def add_peek_pass_button_clicked(self):
        self.add_peek_pass_bool = not self.add_peek_pass_bool
        if self.add_peek_pass_bool:
            self.add_ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.add_ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def generate_pass_button_clicked(self):
        password = backend.generate_password()
        self.add_ui.passwordLineEdit.setText(password)
        self.add_ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.add_peek_pass_bool = True


if __name__ == "__main__":
    app_id = "DylanFarrar.passwordmanager.01"                      
    QtWin.setCurrentProcessExplicitAppUserModelID(app_id)           # this sets a custom app id so that my icon is shown instead of the python icon
    backend = PasswordManager()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    app.setWindowIcon(QtGui.QIcon("assets/icon.ico"))
    app.setStyle("Fusion")
    ui.setupUi()
    if backend.first_run:
        ui.setup_promot()
    else:
        ui.password_prompt()
    sys.exit(app.exec_())
