from views import form4_view
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Form4_manger(QtWidgets.QWidget, form4_view.Ui_Form):
    def __init__(self):
        super(Form4_manger, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = Form4_manger()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
