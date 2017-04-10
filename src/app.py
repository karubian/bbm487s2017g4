from PyQt5 import QtWidgets

import views.LoginView as LoginController

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startApp = LoginController.LoginView()
    startApp.show()
    sys.exit(app.exec_())
