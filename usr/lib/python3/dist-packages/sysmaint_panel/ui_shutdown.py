


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShutdownDialog(object):
    def setupUi(self, ShutdownDialog):
        ShutdownDialog.setObjectName("ShutdownDialog")
        ShutdownDialog.resize(353, 86)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShutdownDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ShutdownDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.yesButton = QtWidgets.QPushButton(ShutdownDialog)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtWidgets.QPushButton(ShutdownDialog)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ShutdownDialog)
        QtCore.QMetaObject.connectSlotsByName(ShutdownDialog)

    def retranslateUi(self, ShutdownDialog):
        _translate = QtCore.QCoreApplication.translate
        ShutdownDialog.setWindowTitle(_translate("ShutdownDialog", "Shut Down"))
        self.label.setText(_translate("ShutdownDialog", "Are you sure you want to shut down the system?"))
        self.yesButton.setText(_translate("ShutdownDialog", "Yes"))
        self.noButton.setText(_translate("ShutdownDialog", "No"))
