


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BackgroundScreen(object):
    def setupUi(self, BackgroundScreen):
        BackgroundScreen.setObjectName("BackgroundScreen")
        BackgroundScreen.resize(400, 300)
        BackgroundScreen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3b187b, stop:1 #a9def2);")

        self.retranslateUi(BackgroundScreen)
        QtCore.QMetaObject.connectSlotsByName(BackgroundScreen)

    def retranslateUi(self, BackgroundScreen):
        _translate = QtCore.QCoreApplication.translate
        BackgroundScreen.setWindowTitle(_translate("BackgroundScreen", "Background Window"))
