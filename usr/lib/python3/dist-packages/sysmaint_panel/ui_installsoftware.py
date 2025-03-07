


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InstallSoftwareDialog(object):
    def setupUi(self, InstallSoftwareDialog):
        InstallSoftwareDialog.setObjectName("InstallSoftwareDialog")
        InstallSoftwareDialog.resize(331, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(InstallSoftwareDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(InstallSoftwareDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.packageLineEdit = QtWidgets.QLineEdit(InstallSoftwareDialog)
        self.packageLineEdit.setObjectName("packageLineEdit")
        self.verticalLayout.addWidget(self.packageLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.searchButton = QtWidgets.QPushButton(InstallSoftwareDialog)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.installButton = QtWidgets.QPushButton(InstallSoftwareDialog)
        self.installButton.setObjectName("installButton")
        self.horizontalLayout.addWidget(self.installButton)
        self.cancelButton = QtWidgets.QPushButton(InstallSoftwareDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(InstallSoftwareDialog)
        QtCore.QMetaObject.connectSlotsByName(InstallSoftwareDialog)

    def retranslateUi(self, InstallSoftwareDialog):
        _translate = QtCore.QCoreApplication.translate
        InstallSoftwareDialog.setWindowTitle(_translate("InstallSoftwareDialog", "Install Software"))
        self.label.setText(_translate("InstallSoftwareDialog", "Enter a package name to install or search for:"))
        self.searchButton.setText(_translate("InstallSoftwareDialog", "Search"))
        self.installButton.setText(_translate("InstallSoftwareDialog", "Install"))
        self.cancelButton.setText(_translate("InstallSoftwareDialog", "Cancel"))
