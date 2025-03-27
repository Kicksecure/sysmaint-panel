


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WrongUserDialog(object):
    def setupUi(self, WrongUserDialog):
        WrongUserDialog.setObjectName("WrongUserDialog")
        WrongUserDialog.resize(412, 174)
        self.verticalLayout = QtWidgets.QVBoxLayout(WrongUserDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(WrongUserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(400, 0))
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(WrongUserDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(WrongUserDialog)
        QtCore.QMetaObject.connectSlotsByName(WrongUserDialog)

    def retranslateUi(self, WrongUserDialog):
        _translate = QtCore.QCoreApplication.translate
        WrongUserDialog.setWindowTitle(_translate("WrongUserDialog", "Insufficient Privileges"))
        self.label.setText(_translate("WrongUserDialog", "<html><head/><body><p>This system is currently configured to only allow the<br>\n"
"\'sysmaint\' account to perform system maintenance.<br>\n"
"Please log into the \'sysmaint\' user account.</p>\n"
"<p>See <a href=\"https://www.kicksecure.com/wiki/sysmaint\">https://www.kicksecure.com/wiki/Sysmaint</a> for more<br>\n"
"information.</p></body></html>"))
        self.okButton.setText(_translate("WrongUserDialog", "OK"))
