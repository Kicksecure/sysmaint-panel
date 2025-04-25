


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageSoftwareDialog(object):
    def setupUi(self, ManageSoftwareDialog):
        ManageSoftwareDialog.setObjectName("ManageSoftwareDialog")
        ManageSoftwareDialog.resize(354, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(ManageSoftwareDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ManageSoftwareDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.packageLineEdit = QtWidgets.QLineEdit(ManageSoftwareDialog)
        self.packageLineEdit.setObjectName("packageLineEdit")
        self.verticalLayout.addWidget(self.packageLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(ManageSoftwareDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.actionComboBox = QtWidgets.QComboBox(ManageSoftwareDialog)
        self.actionComboBox.setObjectName("actionComboBox")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.horizontalLayout.addWidget(self.actionComboBox)
        self.runButton = QtWidgets.QPushButton(ManageSoftwareDialog)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.cancelButton = QtWidgets.QPushButton(ManageSoftwareDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ManageSoftwareDialog)
        QtCore.QMetaObject.connectSlotsByName(ManageSoftwareDialog)

    def retranslateUi(self, ManageSoftwareDialog):
        _translate = QtCore.QCoreApplication.translate
        ManageSoftwareDialog.setWindowTitle(_translate("ManageSoftwareDialog", "Manage Software"))
        self.label.setText(_translate("ManageSoftwareDialog", "Enter a package name to search or modify:"))
        self.label_2.setText(_translate("ManageSoftwareDialog", "Action:"))
        self.actionComboBox.setItemText(0, _translate("ManageSoftwareDialog", "Search"))
        self.actionComboBox.setItemText(1, _translate("ManageSoftwareDialog", "Install"))
        self.actionComboBox.setItemText(2, _translate("ManageSoftwareDialog", "Reinstall"))
        self.actionComboBox.setItemText(3, _translate("ManageSoftwareDialog", "Remove"))
        self.actionComboBox.setItemText(4, _translate("ManageSoftwareDialog", "Purge"))
        self.actionComboBox.setItemText(5, _translate("ManageSoftwareDialog", "Override"))
        self.actionComboBox.setItemText(6, _translate("ManageSoftwareDialog", "Help"))
        self.runButton.setText(_translate("ManageSoftwareDialog", "Run"))
        self.cancelButton.setText(_translate("ManageSoftwareDialog", "Cancel"))
