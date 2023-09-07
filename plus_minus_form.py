from PySide6 import QtWidgets, QtGui

from ui.ui_plus_minus_form import Ui_PlusMinusForm
import ui.plus_minus_resource_rc


class PlusMinusForm(QtWidgets.QWidget, Ui_PlusMinusForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Plus minus form")
        self.spin_box.setValue(50)
        plus_icon = QtGui.QIcon(":/images/plus.png")
        minus_icon = QtGui.QIcon(":/images/minus.png")
        self.minus_button.setIcon(minus_icon)
        self.plus_button.setIcon(plus_icon)
        self.minus_button.clicked.connect(self.plus)
        self.plus_button.clicked.connect(self.minus)

    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value + 1)

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value - 1)
