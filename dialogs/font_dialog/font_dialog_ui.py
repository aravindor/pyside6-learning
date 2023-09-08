from PySide6 import QtWidgets

from dialogs.font_dialog.ui_font_dialog import Ui_Form


class FontDialog(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Choose font")
        self.pushButton.clicked.connect(self.button_click)

    def button_click(self):
        font = QtWidgets.QFontDialog.getFont(self)
        self.label.setFont(font)

