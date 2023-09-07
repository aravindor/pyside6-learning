from PySide6 import QtWidgets

from window.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Text editor example")
        self.actionQuit.triggered.connect(lambda: self.close())
        self.actionCopy.triggered.connect(lambda: self.textEdit.copy())
        self.actionCut.triggered.connect(lambda: self.textEdit.cut())
        self.actionPaste.triggered.connect(lambda: self.textEdit.paste())
        self.actionUndo.triggered.connect(lambda: self.textEdit.undo())
        self.actionRedo.triggered.connect(lambda: self.textEdit.redo())
        self.actionAbout.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, "About", "Qt is awesome"))
