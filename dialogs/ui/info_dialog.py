from PySide6 import QtWidgets

from dialogs.ui.ui_info_dialog import Ui_Dialog


class InfoDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Provide information")
        self.setupUi(self)
        self.position = ""
        self.os = ""
        self.pushButton.clicked.connect(self.ok)
        self.pushButton_2.clicked.connect(self.reject)

    def ok(self):
        if not self.position_line_edit.text() == "":
            self.position = self.position_line_edit.text()
        self.os = self.os_combo_box.currentText()
        self.accept()
