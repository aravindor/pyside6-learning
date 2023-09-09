from PySide6 import QtWidgets

from dialogs.file_dialog.ui_file_picker import Ui_Form


class FilePicker(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("File picker demo")
        self.pushButton.clicked.connect(self.set_button_click)

    def set_button_click(self):
        # directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open directory", "/home", )
        # print(directory)
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "/home", )
        print(file)
