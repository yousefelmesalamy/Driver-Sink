from views import form1_view
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Form1_manger(QtWidgets.QWidget, form1_view.Ui_Form):
    def __init__(self):
        super(Form1_manger, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = Form1_manger()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
