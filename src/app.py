from PyQt5 import QtCore, QtGui, QtWidgets
import controllers.LoginController as LoginController

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    startApp = LoginController.LoginController()
    startApp.show()
    sys.exit(app.exec_())