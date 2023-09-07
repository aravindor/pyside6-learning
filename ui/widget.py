from PySide6 import QtWidgets, QtUiTools

from ui.ui_widget import Ui_Widget


class Widget(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Widget generator demo")

