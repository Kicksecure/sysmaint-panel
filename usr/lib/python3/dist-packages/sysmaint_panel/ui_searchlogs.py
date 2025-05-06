


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchLogsDialog(object):
    def setupUi(self, SearchLogsDialog):
        SearchLogsDialog.setObjectName("SearchLogsDialog")
        SearchLogsDialog.resize(491, 124)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchLogsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SearchLogsDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.searchTermLineEdit = QtWidgets.QLineEdit(SearchLogsDialog)
        self.searchTermLineEdit.setObjectName("searchTermLineEdit")
        self.horizontalLayout.addWidget(self.searchTermLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(SearchLogsDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.searchButton = QtWidgets.QPushButton(SearchLogsDialog)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.cancelButton = QtWidgets.QPushButton(SearchLogsDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SearchLogsDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchLogsDialog)

    def retranslateUi(self, SearchLogsDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchLogsDialog.setWindowTitle(_translate("SearchLogsDialog", "Search Logs"))
        self.label.setText(_translate("SearchLogsDialog", "Search term:"))
        self.label_2.setText(_translate("SearchLogsDialog", "Note: grep-compatible extended regular expressions are supported."))
        self.searchButton.setText(_translate("SearchLogsDialog", "Search"))
        self.cancelButton.setText(_translate("SearchLogsDialog", "Cancel"))
