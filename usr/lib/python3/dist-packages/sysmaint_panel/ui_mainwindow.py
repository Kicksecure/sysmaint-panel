


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.installationGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.installationGroupBox.setObjectName("installationGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.installationGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.installSystemButton = QtWidgets.QPushButton(self.installationGroupBox)
        self.installSystemButton.setObjectName("installSystemButton")
        self.gridLayout_4.addWidget(self.installSystemButton, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.installationGroupBox)
        self.softwareUpdatesGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.softwareUpdatesGroupBox.setObjectName("softwareUpdatesGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.softwareUpdatesGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.purgeUnusedPackagesButton = QtWidgets.QPushButton(self.softwareUpdatesGroupBox)
        self.purgeUnusedPackagesButton.setObjectName("purgeUnusedPackagesButton")
        self.gridLayout.addWidget(self.purgeUnusedPackagesButton, 1, 1, 1, 1)
        self.checkForUpdatesButton = QtWidgets.QPushButton(self.softwareUpdatesGroupBox)
        self.checkForUpdatesButton.setObjectName("checkForUpdatesButton")
        self.gridLayout.addWidget(self.checkForUpdatesButton, 0, 0, 1, 1)
        self.removeUnusedPackagesButton = QtWidgets.QPushButton(self.softwareUpdatesGroupBox)
        self.removeUnusedPackagesButton.setObjectName("removeUnusedPackagesButton")
        self.gridLayout.addWidget(self.removeUnusedPackagesButton, 0, 1, 1, 1)
        self.installUpdatesButton = QtWidgets.QPushButton(self.softwareUpdatesGroupBox)
        self.installUpdatesButton.setObjectName("installUpdatesButton")
        self.gridLayout.addWidget(self.installUpdatesButton, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.softwareUpdatesGroupBox)
        self.systemAdministrationGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.systemAdministrationGroupBox.setObjectName("systemAdministrationGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.systemAdministrationGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.removeUserButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.removeUserButton.setObjectName("removeUserButton")
        self.gridLayout_2.addWidget(self.removeUserButton, 2, 1, 1, 1)
        self.createUserButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.createUserButton.setObjectName("createUserButton")
        self.gridLayout_2.addWidget(self.createUserButton, 1, 1, 1, 1)
        self.manageAutologinButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.manageAutologinButton.setObjectName("manageAutologinButton")
        self.gridLayout_2.addWidget(self.manageAutologinButton, 2, 0, 1, 1)
        self.checkSystemStatusButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.checkSystemStatusButton.setObjectName("checkSystemStatusButton")
        self.gridLayout_2.addWidget(self.checkSystemStatusButton, 3, 0, 1, 1)
        self.managePasswordsButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.managePasswordsButton.setObjectName("managePasswordsButton")
        self.gridLayout_2.addWidget(self.managePasswordsButton, 1, 0, 1, 1)
        self.runRepositoryWizardButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.runRepositoryWizardButton.setObjectName("runRepositoryWizardButton")
        self.gridLayout_2.addWidget(self.runRepositoryWizardButton, 3, 1, 1, 1)
        self.manageSoftwareButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.manageSoftwareButton.setObjectName("manageSoftwareButton")
        self.gridLayout_2.addWidget(self.manageSoftwareButton, 4, 0, 1, 1)
        self.searchLogsButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.searchLogsButton.setObjectName("searchLogsButton")
        self.gridLayout_2.addWidget(self.searchLogsButton, 4, 1, 1, 1)
        self.networkConnButton = QtWidgets.QPushButton(self.systemAdministrationGroupBox)
        self.networkConnButton.setObjectName("networkConnButton")
        self.gridLayout_2.addWidget(self.networkConnButton, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.systemAdministrationGroupBox)
        self.miscGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.miscGroupBox.setObjectName("miscGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.miscGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.openTerminalButton = QtWidgets.QPushButton(self.miscGroupBox)
        self.openTerminalButton.setObjectName("openTerminalButton")
        self.gridLayout_5.addWidget(self.openTerminalButton, 0, 0, 1, 1)
        self.rebootButton = QtWidgets.QPushButton(self.miscGroupBox)
        self.rebootButton.setObjectName("rebootButton")
        self.gridLayout_5.addWidget(self.rebootButton, 0, 1, 1, 1)
        self.lockScreenButton = QtWidgets.QPushButton(self.miscGroupBox)
        self.lockScreenButton.setObjectName("lockScreenButton")
        self.gridLayout_5.addWidget(self.lockScreenButton, 1, 0, 1, 1)
        self.shutDownButton = QtWidgets.QPushButton(self.miscGroupBox)
        self.shutDownButton.setObjectName("shutDownButton")
        self.gridLayout_5.addWidget(self.shutDownButton, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.miscGroupBox)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System Maintenance Panel"))
        self.label.setText(_translate("MainWindow", "<h1>System Maintenance Panel</h1>"))
        self.installationGroupBox.setTitle(_translate("MainWindow", "Installation"))
        self.installSystemButton.setText(_translate("MainWindow", "Install System"))
        self.softwareUpdatesGroupBox.setTitle(_translate("MainWindow", "Software Updates"))
        self.purgeUnusedPackagesButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Removes packages that the OS and manually installed applications do not depend on. Also cleans up unneeded configuration files.</p></body></html>"))
        self.purgeUnusedPackagesButton.setText(_translate("MainWindow", "Purge Unused Packages"))
        self.checkForUpdatesButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Checks for software updates for all apt packages on the system. This will find updates for the OS and for applications installed via the apt package manager.</p></body></html>"))
        self.checkForUpdatesButton.setText(_translate("MainWindow", "Check for Updates"))
        self.removeUnusedPackagesButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Removes packages that the OS and manually installed applications do not depend on.</p></body></html>"))
        self.removeUnusedPackagesButton.setText(_translate("MainWindow", "Remove Unused Packages"))
        self.installUpdatesButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Installs OS and application updates. If necessary, this will check for updates before attempting to install them.</p></body></html>"))
        self.installUpdatesButton.setText(_translate("MainWindow", "Install Updates"))
        self.systemAdministrationGroupBox.setTitle(_translate("MainWindow", "System Administration"))
        self.removeUserButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Deletes an existing user account. <span style=\" font-weight:600;\">This cannot be undone!</span></p></body></html>"))
        self.removeUserButton.setText(_translate("MainWindow", "Remove User"))
        self.createUserButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Creates a new user account.</p></body></html>"))
        self.createUserButton.setText(_translate("MainWindow", "Create User"))
        self.manageAutologinButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enables or disables autologin for a user account.</p></body></html>"))
        self.manageAutologinButton.setText(_translate("MainWindow", "Manage GUI Autologin"))
        self.checkSystemStatusButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Runs the System Check utility.</p></body></html>"))
        self.checkSystemStatusButton.setText(_translate("MainWindow", "Check System Status"))
        self.managePasswordsButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Changes the password for a user account.</p></body></html>"))
        self.managePasswordsButton.setText(_translate("MainWindow", "Manage Passwords"))
        self.runRepositoryWizardButton.setText(_translate("MainWindow", "Run Repository Wizard"))
        self.manageSoftwareButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Allows you to search for and install software through the apt package manager.</p></body></html>"))
        self.manageSoftwareButton.setText(_translate("MainWindow", "Manage Software"))
        self.searchLogsButton.setText(_translate("MainWindow", "Search Logs"))
        self.networkConnButton.setText(_translate("MainWindow", "Network and Internet Connections"))
        self.miscGroupBox.setTitle(_translate("MainWindow", "Misc"))
        self.openTerminalButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Opens a terminal window. Use this for advanced maintenance tasks.</p></body></html>"))
        self.openTerminalButton.setText(_translate("MainWindow", "Open Terminal"))
        self.rebootButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Reboots the system.</p></body></html>"))
        self.rebootButton.setText(_translate("MainWindow", "Reboot"))
        self.lockScreenButton.setText(_translate("MainWindow", "Lock Screen"))
        self.shutDownButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shuts down the system.</p></body></html>"))
        self.shutDownButton.setText(_translate("MainWindow", "Shut Down"))
