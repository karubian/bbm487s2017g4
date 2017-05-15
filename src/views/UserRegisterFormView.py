from PyQt5 import QtCore, QtGui, QtWidgets
from views.gen.Ui_userRegisterForm import Ui_userRegisterForm
from controllers.UserController import UserController
import views.ErrorView as errorView


class UserRegisterFormView(Ui_userRegisterForm):
    def __init__(self):
        self.userRegisterFormScreen = QtWidgets.QDialog()
        self.ui = Ui_userRegisterForm()
        self.userController = UserController()
        self.ui.setupUi(self.userRegisterFormScreen)
        self.ui.registerButton.clicked.connect(self.register_user)
        self.ui.cancelButton.clicked.connect(self.terminate)
        self.error = errorView.ErrorView()
        self.currentUser = None
        self.type = 0  # 0 for create user 1 for update user
        self.set_button_effects()

    def show(self):
        self.userRegisterFormScreen.show()

    def terminate(self):
        self.userRegisterFormScreen.hide()

    def clear_forms(self):
        self.ui.usernameLineEdit.setText("")
        self.ui.passwordLineEdit.setText("")
        self.ui.nameLineEdit.setText("")
        self.ui.surnameLineEdit.setText("")
        self.ui.emailLineEdit.setText("")

    def prepare_update(self, user):
        self.ui.usernameLineEdit.setText(user.username)
        self.ui.passwordLineEdit.setText(user.password)
        self.ui.nameLineEdit.setText(user.name)
        self.ui.surnameLineEdit.setText(user.surname)
        self.ui.emailLineEdit.setText(user.email_address)

    def register_user(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        name = self.ui.nameLineEdit.text()
        surname = self.ui.surnameLineEdit.text()
        email = self.ui.emailLineEdit.text()
        validation_flag = 0
        error_flag = 0
        if self.type is 0:
            for field in [username, password, name, surname, email]:
                if len(field) == 0:
                    validation_flag = 1
            if validation_flag is 0:
                if self.userController.add_new_member(username, password, name, surname, email) is None:
                    self.error.set_error_text("Username already exists!")
                    error_flag = 1
                    self.error.errorScreen.exec_()
            else:
                self.error.set_error_text("Please fill the blank fields.")
                self.error.errorScreen.exec_()
        elif self.type is 1:
            for field in [username, password, name, surname, email]:
                if len(field) == 0:
                    validation_flag = 1
            if validation_flag is 0:
                self.userController.update_member([username, password, email, name, surname], self.currentUser)
            else:
                self.error.set_error_text("Please fill the blank fields.")
                self.error.errorScreen.exec_()
        if error_flag is 0:
            self.userRegisterFormScreen.hide()
            self.clear_forms()

    def set_button_effects(self):
        self.ui.registerButton.released.connect(self.released_color_change)
        self.ui.registerButton.pressed.connect(self.pressed_color_change)
        self.ui.cancelButton.released.connect(self.released_color_change)
        self.ui.cancelButton.pressed.connect(self.pressed_color_change)

    def released_color_change(self):
        self.userRegisterFormScreen.sender().setStyleSheet("QPushButton {\n"
                                                           "color: white;\n"
                                                           "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dd7a23, stop: 0.1 #e87919, stop: 0.49 #ce650a, stop: 0.5 #c45d03, stop: 1 #d16304);\n"
                                                           "font-size: 30px;\n"
                                                           "border-radius:10px;\n"
                                                           "}")

    def pressed_color_change(self):
        self.userRegisterFormScreen.sender().setStyleSheet("QPushButton {\n"
                                                           "color: white;\n"
                                                           "background-color: red;\n"
                                                           "font-size: 30px;\n"
                                                           "border-radius:10px;\n"
                                                           "}")
