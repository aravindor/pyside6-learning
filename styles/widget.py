from PySide6 import QtWidgets

from styles.ui_widget import Ui_Form


class StyledWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled QT")
        self.setupUi(self)
