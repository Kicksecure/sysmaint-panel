


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageSoftwareHelpDialog(object):
    def setupUi(self, ManageSoftwareHelpDialog):
        ManageSoftwareHelpDialog.setObjectName("ManageSoftwareHelpDialog")
        ManageSoftwareHelpDialog.resize(473, 404)
        self.verticalLayout = QtWidgets.QVBoxLayout(ManageSoftwareHelpDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ManageSoftwareHelpDialog)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(ManageSoftwareHelpDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ManageSoftwareHelpDialog)
        QtCore.QMetaObject.connectSlotsByName(ManageSoftwareHelpDialog)

    def retranslateUi(self, ManageSoftwareHelpDialog):
        _translate = QtCore.QCoreApplication.translate
        ManageSoftwareHelpDialog.setWindowTitle(_translate("ManageSoftwareHelpDialog", "Help - Manage Software"))
        self.label.setText(_translate("ManageSoftwareHelpDialog", "<html>\n"
"<head/>\n"
"<body>\n"
"<p>The following software management actions are available:</p>\n"
"<ul>\n"
"<li>Search: Looks through all enabled software repositories for<br/>\n"
"a software package.</li>\n"
"<li>Install: Downloads and installs a software package.</li>\n"
"<li>Reinstall: Downloads and installs a software package, even<br/>\n"
"if it is already installed.</li>\n"
"<li>Remove: Uninstalls a software package and anything<br/>\n"
"depending on it. Leaves the package\'s configuration files on<br/>\n"
"the system.</li>\n"
"<li>Purge: Uninstalls a software package and anything<br/>\n"
"depending on it. Wipes the package\'s configuration files.</li>\n"
"<li>Override: Uninstalls a software package without removing<br/>\n"
"other software that depends on it. Removes the package\'s<br/>\n"
"configuration files. Do not use this unless you know what<br/>\n"
"you are doing.<br></li>\n"
"</ul>\n"
"</body>\n"
"</html>"))
        self.okButton.setText(_translate("ManageSoftwareHelpDialog", "OK"))
