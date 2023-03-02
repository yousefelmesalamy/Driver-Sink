from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *

from views_mangers.login_manger import Login_manger
from views_mangers.chose_form_manger import Chose_form_manger


class First(QtWidgets.QStackedWidget):
    def __init__(self):
        super(First, self).__init__()



        self.setMinimumSize(1360,768)

        # install widget
        self.login_manger = Login_manger()
        self.chose_form_manger =  Chose_form_manger()


        # add widget
        self.addWidget(self.login_manger) #0
        self.addWidget(self.chose_form_manger) #1


        #install login screen signal
        self.login_manger.login_accept_signal.connect(self.handle_login)

        # choose screen
        self.chose_form_manger.logout_btn.clicked.connect(self.handel_sign)

    def handel_sign(self):
        self.login_manger.username_lin.clear()
        self.login_mangE4er.password_lin.clear()
        self.setCurrentIndex(0)
    def handle_login(self):
        self.chose_form_manger.username_lbl.setText(self.login_manger.username_lin.text())
        self.chose_form_manger.thread.start()
        self.setCurrentIndex(1)





if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = First()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
