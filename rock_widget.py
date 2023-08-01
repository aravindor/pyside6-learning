from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing layout")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        button1.clicked.connect(lambda: print("Clicked button1"))
        button2.clicked.connect(lambda: print("Clicked button2"))

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        self.setLayout(button_layout)
        button_layout.addWidget(button2)
