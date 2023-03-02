from views import form3_view
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Form3_manger(QtWidgets.QWidget, form3_view.Ui_Form):
    def __init__(self):
        super(Form3_manger, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    window = Form3_manger()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
