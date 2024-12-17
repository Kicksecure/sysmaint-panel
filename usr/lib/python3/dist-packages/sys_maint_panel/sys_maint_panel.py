import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from ui_mainwindow import Ui_MainWindow
from ui_reboot import Ui_RebootDialog
from ui_shutdown import Ui_ShutdowDialog
from ui_installsoftware import Ui_InstallSoftwareWindow

class InstallSoftwareWindow(QDialog):
    def __init__(self):
        super(InstallSoftwareWindow, self).__init__()
        self.ui = Ui_InstallSoftwareWindow()
        self.ui.setupUi(self)
        self.resize(self.minimumWidth(), self.minimumHeight())

        self.ui.searchButton.clicked.connect(self.searchForPackage)
        self.ui.installButton.clicked.connect(self.installPackage)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def searchForPackage(self):
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/apt-cache", "search",
                          self.ui.packageLineEdit.text()])
        print(1)

    def installPackage(self):
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo", "/usr/bin/apt", "install",
                          self.ui.packageLineEdit.text()])
        self.done(0)

    def cancel(self):
        self.done(0)

class RebootWindow(QDialog):
    def __init__(self):
        super(RebootWindow, self).__init__()
        self.ui = Ui_RebootDialog()
        self.ui.setupUi(self)
        self.resize(self.minimumWidth(), self.minimumHeight())

        self.ui.yesButton.clicked.connect(self.reboot)
        self.ui.noButton.clicked.connect(self.cancel)

    @staticmethod
    def reboot():
        subprocess.run(["/usr/sbin/reboot"])

    def cancel(self):
        self.done(0)

class ShutdownWindow(QDialog):
    def __init__(self):
        super(ShutdownWindow, self).__init__()
        self.ui = Ui_ShutdowDialog()
        self.ui.setupUi(self)
        self.resize(self.minimumWidth(), self.minimumHeight())

        self.ui.yesButton.clicked.connect(self.shutdown)
        self.ui.noButton.clicked.connect(self.cancel)

    @staticmethod
    def shutdown():
        subprocess.run(["/usr/sbin/shutdown", "now"])

    def cancel(self):
        self.done(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(self.minimumWidth(), self.minimumHeight())

        self.ui.checkForUpdatesButton.clicked.connect(self.check_for_updates)
        self.ui.installUpdatesButton.clicked.connect(self.install_updates)
        self.ui.removeUnusedPackagesButton.clicked.connect(self.remove_unused_packages)
        self.ui.purgeUnusedPackagesButton.clicked.connect(self.purge_unused_packages)

        self.ui.installSoftwareButton.clicked.connect(self.install_software)
        self.ui.changePasswordButton.clicked.connect(self.change_password)
        self.ui.createUserButton.clicked.connect(self.create_user)
        self.ui.removeUserButton.clicked.connect(self.remove_user)

        self.ui.openTerminalButton.clicked.connect(self.open_terminal)
        self.ui.rebootButton.clicked.connect(self.reboot)
        self.ui.shutDownButton.clicked.connect(self.shutdown)

    @staticmethod
    def check_for_updates():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo", "/usr/bin/apt", "update"])

    @staticmethod
    def install_updates():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo", "/usr/bin/apt",
                          "full-upgrade"])

    @staticmethod
    def remove_unused_packages():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo", "/usr/bin/apt", "autoremove"])

    @staticmethod
    def purge_unused_packages():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo", "/usr/bin/apt", "autopurge"])

    @staticmethod
    def install_software():
        install_software_window = InstallSoftwareWindow()
        install_software_window.exec()

    @staticmethod
    def change_password():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo",
                          "/usr/libexec/sys-maint-panel/change-user-password"])

    @staticmethod
    def create_user():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                         "/usr/bin/sudo",
                         "/usr/libexec/sys-maint-panel/create-user"])

    @staticmethod
    def remove_user():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                          "/usr/bin/sudo", "/usr/sbin/deluser"])

    @staticmethod
    def open_terminal():
        subprocess.Popen(["/usr/libexec/helper-scripts/terminal-wrapper",
                         "/bin/bash"])

    @staticmethod
    def reboot():
        reboot_window = RebootWindow()
        reboot_window.exec()

    @staticmethod
    def shutdown():
        shutdown_window = ShutdownWindow()
        shutdown_window.exec()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()