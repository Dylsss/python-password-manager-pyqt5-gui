
from PyQt5 import QtCore, QtGui, QtWidgets


class Setup_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 51))
        self.label.setObjectName("label")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 80, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.passwordLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.passwordLineEdit)
        
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswordLineEdit.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.confirmPasswordLineEdit)
        
        self.setupPushButton = QtWidgets.QPushButton(Dialog)
        self.setupPushButton.setGeometry(QtCore.QRect(190, 170, 75, 23))
        self.setupPushButton.setObjectName("pushButton")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setup"))
        self.label.setText(_translate("Dialog", "This is your first time opening this program, please set a password for your\n"
"password manager. You cannot reset it if you forget!"))
        self.passwordLineEdit.setPlaceholderText(_translate("Dialog", "Enter password"))
        self.confirmPasswordLineEdit.setPlaceholderText(_translate("Dialog", "Confirm password"))
        self.setupPushButton.setText(_translate("Dialog", "Continue"))
        self.label_2.setText(_translate("Dialog", "Passwords don\'t match"))