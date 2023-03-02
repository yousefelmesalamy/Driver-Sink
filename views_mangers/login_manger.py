from views import login_view
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Login_manger(QtWidgets.QWidget, login_view.Ui_Form) :
    login_accept_signal = pyqtSignal()
    def __init__(self):
        super(Login_manger, self).__init__()
        self.setupUi(self)
        self.users = {"yosef@gmail.com":"122122","1":"1"}

        self.login_btn.clicked.connect(self.run)

    def run(self):
        try :
            username = self.username_lin.text()
            password = self.password_lin.text()
            if username in self.users.keys():
                if password == self.users[username]:
                    print('login success')
                    self.login_accept_signal.emit()
            else:
                print('fail')
        except Exception as e :
            print(e)

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = Login_manger()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
