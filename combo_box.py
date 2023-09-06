from PySide6 import QtWidgets


class ComboBoxWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo box")
        self.combo_box = QtWidgets.QComboBox(self)

        self.combo_box.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])
        button_current = QtWidgets.QPushButton("Current value")
        button_current.clicked.connect(
            lambda: print(f"{self.combo_box.currentText()} [{self.combo_box.currentIndex()} ]"))
        button_set_current = QtWidgets.QPushButton("Set current")
        button_set_current.clicked.connect(lambda: self.combo_box.setCurrentIndex(2))
        button_get_current = QtWidgets.QPushButton("Get current")

        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_current)
        self.setLayout(v_layout)
