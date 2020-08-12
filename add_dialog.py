from PyQt5 import QtCore, QtWidgets, QtGui

class Add_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(328, 178)
        
        self.accountLineEdit = QtWidgets.QLineEdit(Dialog)
        self.accountLineEdit.setGeometry(QtCore.QRect(80, 30, 161, 20))
        self.accountLineEdit.setObjectName("accountLineEdit")
        self.accountLineEdit.setPlaceholderText("Enter account name")
        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(80, 60, 161, 20))
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.usernameLineEdit.setPlaceholderText("Enter username")
        
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(80, 90, 161, 20))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setPlaceholderText("Enter password")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.addEntryButton = QtWidgets.QPushButton(Dialog)
        self.addEntryButton.setGeometry(QtCore.QRect(190, 120, 51, 23))
        self.addEntryButton.setObjectName("addEntryButton")
        
        self.generatePassButton = QtWidgets.QPushButton(Dialog)
        self.generatePassButton.setGeometry(QtCore.QRect(80, 120, 101, 23))
        self.generatePassButton.setObjectName("generatePassButton")
        
        self.peekPassButton = QtWidgets.QPushButton(Dialog)
        self.peekPassButton.setGeometry(QtCore.QRect(250, 90, 31, 21))
        self.peekPassButton.setText("")
        self.peekPassButton.setIcon(QtGui.QIcon("assets/eye_icon.ico"))
        self.peekPassButton.setObjectName("peekPassButton")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 150, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add entry"))
        self.addEntryButton.setText(_translate("Dialog", "Add entry"))
        self.generatePassButton.setText(_translate("Dialog", "Generate password"))
        self.label_2.setText(_translate("Dialog", "Not all text fields are filled"))