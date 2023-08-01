from PySide6.QtWidgets import QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        button = QPushButton(text="Click me")
        button.setCheckable(True)
        button.clicked.connect(lambda data: print("Clicked",data))
        self.setCentralWidget(button)
