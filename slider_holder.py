from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QSlider


class SliderHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkout this slider")
        slider = QSlider(orientation=Qt.Orientation.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setPageStep(5)
        slider.valueChanged.connect(lambda value: print(value))
        self.setCentralWidget(slider)
