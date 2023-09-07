from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()


class UserInterFace(QtCore.QObject):
    def __init__(self):
        super().__init__()

        self.ui = loader.load("ui/widget.ui")
        self.ui.setWindowTitle("Qt loader demo")

    def show(self):
        self.ui.show()
