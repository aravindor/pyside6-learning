from PySide6 import QtWidgets


class GridLayoutWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid demo")
        button_1 = QtWidgets.QPushButton("Button 1")
        button_1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_2 = QtWidgets.QPushButton("Button 2")
        button_2.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_3 = QtWidgets.QPushButton("Button 3")
        button_3.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_4 = QtWidgets.QPushButton("Button 4")
        button_4.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_5 = QtWidgets.QPushButton("Button 5")
        button_5.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_6 = QtWidgets.QPushButton("Button 6")
        button_6.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_7 = QtWidgets.QPushButton("Button 7")
        button_7.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_8 = QtWidgets.QPushButton("Button 8")
        button_8.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_9 = QtWidgets.QPushButton("Button 9")
        button_9.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(button_1, 0, 0)
        grid.addWidget(button_2, 0, 1)
        grid.addWidget(button_3, 0, 2)
        grid.addWidget(button_4, 1, 0)
        grid.addWidget(button_5, 1, 1)
        grid.addWidget(button_6, 1, 2)
        grid.addWidget(button_7, 2, 0)
        grid.addWidget(button_8, 2, 1)
        grid.addWidget(button_9, 2, 2)

        self.setLayout(grid)
