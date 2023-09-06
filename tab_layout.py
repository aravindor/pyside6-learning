from PySide6 import QtWidgets


class TabWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab demo')

        tab_1 = QtWidgets.QWidget()
        button1 = QtWidgets.QPushButton("Button 1")
        button2 = QtWidgets.QPushButton("Button 2")
        button3 = QtWidgets.QPushButton("Button 3")
        tab_1_layout = QtWidgets.QVBoxLayout()
        tab_1_layout.addWidget(button1)
        tab_1_layout.addWidget(button2)
        tab_1_layout.addWidget(button3)
        tab_1.setLayout(tab_1_layout)

        tab_2 = QtWidgets.QWidget()
        button4 = QtWidgets.QPushButton("Button 4")
        button5 = QtWidgets.QPushButton("Button 5")
        button6 = QtWidgets.QPushButton("Button 6")
        tab_2_layout = QtWidgets.QVBoxLayout()
        tab_2_layout.addWidget(button4)
        tab_2_layout.addWidget(button5)
        tab_2_layout.addWidget(button6)
        tab_2.setLayout(tab_2_layout)

        tab = QtWidgets.QTabWidget()
        tab.addTab(tab_1, "Tab 1")
        tab.addTab(tab_2, "Tab 2")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(tab)
        self.setLayout(layout)
