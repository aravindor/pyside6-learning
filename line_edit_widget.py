from PySide6 import QtWidgets


class LineEditWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line edit demo")
        label = QtWidgets.QLabel("Enter name :")
        self.line_edit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton("Grab data")
        self.text_holder_label = QtWidgets.QLabel("I am here")
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)
        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)
        self.setLayout(v_layout)

        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print(self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
