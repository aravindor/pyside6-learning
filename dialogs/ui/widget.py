from PySide6 import QtWidgets

from dialogs.ui.info_dialog import InfoDialog
from dialogs.ui.ui_info_dialog import Ui_Dialog
from dialogs.ui.ui_widget import Ui_DialogWidget


class SimpleInputDialog(QtWidgets.QWidget, Ui_DialogWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple dialog")
        self.setupUi(self)
        self.info_dialog = InfoDialog()
        self.provide_info_button.clicked.connect(self.provide_info)

    def provide_info(self):
        ret = self.info_dialog.exec()
        print(ret)
        if ret == QtWidgets.QDialog.Accepted:
            self.info_label.setText(
                f"Your position is : {self.info_dialog.position} \n Your Os is {self.info_dialog.os}")
        else:
            print("Dialog rejected")
