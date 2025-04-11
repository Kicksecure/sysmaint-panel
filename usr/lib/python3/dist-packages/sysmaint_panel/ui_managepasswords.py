


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManagePasswordsDialog(object):
    def setupUi(self, ManagePasswordsDialog):
        ManagePasswordsDialog.setObjectName("ManagePasswordsDialog")
        ManagePasswordsDialog.resize(324, 80)
        self.verticalLayout = QtWidgets.QVBoxLayout(ManagePasswordsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.userPasswordButton = QtWidgets.QPushButton(ManagePasswordsDialog)
        self.userPasswordButton.setObjectName("userPasswordButton")
        self.gridLayout.addWidget(self.userPasswordButton, 1, 0, 1, 1)
        self.bootloaderPasswordButton = QtWidgets.QPushButton(ManagePasswordsDialog)
        self.bootloaderPasswordButton.setObjectName("bootloaderPasswordButton")
        self.gridLayout.addWidget(self.bootloaderPasswordButton, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(ManagePasswordsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(ManagePasswordsDialog)
        QtCore.QMetaObject.connectSlotsByName(ManagePasswordsDialog)

    def retranslateUi(self, ManagePasswordsDialog):
        _translate = QtCore.QCoreApplication.translate
        ManagePasswordsDialog.setWindowTitle(_translate("ManagePasswordsDialog", "Manage Passwords"))
        self.userPasswordButton.setText(_translate("ManagePasswordsDialog", "User Password"))
        self.bootloaderPasswordButton.setText(_translate("ManagePasswordsDialog", "Bootloader Password"))
        self.label.setText(_translate("ManagePasswordsDialog", "Manage Passwords"))
