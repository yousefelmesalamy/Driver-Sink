from views import form5_view
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Form5_manger(QtWidgets.QWidget, form5_view.Ui_Form):
    def __init__(self):
        super(Form5_manger, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = Form5_manger()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
