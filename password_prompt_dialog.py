from PyQt5 import QtCore, QtGui, QtWidgets

class Password_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(192, 189)
        
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(40, 70, 113, 20))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setPlaceholderText("Enter password")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.enterPasswordPushButton = QtWidgets.QPushButton(Dialog)
        self.enterPasswordPushButton.setGeometry(QtCore.QRect(80, 100, 75, 23))
        self.enterPasswordPushButton.setObjectName("enterPasswordPushButton")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 16))
        self.label.setObjectName("label")
        self.label.hide()
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.enterPasswordPushButton.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Incorrect password"))

