


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BackgroundScreen(object):
    def setupUi(self, BackgroundScreen):
        BackgroundScreen.setObjectName("BackgroundScreen")
        BackgroundScreen.resize(400, 300)
        BackgroundScreen.setStyleSheet("background-color: #000;")

        self.retranslateUi(BackgroundScreen)
        QtCore.QMetaObject.connectSlotsByName(BackgroundScreen)

    def retranslateUi(self, BackgroundScreen):
        _translate = QtCore.QCoreApplication.translate
        BackgroundScreen.setWindowTitle(_translate("BackgroundScreen", "Background Window"))
