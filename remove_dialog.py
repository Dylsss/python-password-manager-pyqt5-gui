from PyQt5 import QtCore, QtWidgets


class Remove_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 178)
        
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(80, 41, 181, 41))
        self.comboBox.setObjectName("comboBox")
        
        self.removeEntryButton = QtWidgets.QPushButton(Dialog)
        self.removeEntryButton.setGeometry(QtCore.QRect(180, 100, 81, 23))
        self.removeEntryButton.setObjectName("removeEntryButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Remove entry"))
        self.removeEntryButton.setText(_translate("Dialog", "Remove"))
