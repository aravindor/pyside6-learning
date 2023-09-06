from PySide6 import QtWidgets


class CheckBoxWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check box tutorial")
        oss = QtWidgets.QGroupBox("Choose OS")
        windows = QtWidgets.QCheckBox("Windows")
        windows.toggled.connect(lambda checked: print(f"Windows checked {checked}"))
        linux = QtWidgets.QCheckBox("Linux")
        linux.toggled.connect(lambda checked: print(f"Linux checked {checked}"))
        mac = QtWidgets.QCheckBox("Mac")
        mac.toggled.connect(lambda checked: print(f"Mac checked {checked}"))

        os_layout = QtWidgets.QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        oss.setLayout(os_layout)

        drinks = QtWidgets.QGroupBox("Choose drink")
        beer = QtWidgets.QCheckBox("Beer")
        tea = QtWidgets.QCheckBox("Beer")
        coffe = QtWidgets.QCheckBox("Coffe")

        exclusive_group = QtWidgets.QButtonGroup(self)
        exclusive_group.addButton(beer)
        exclusive_group.addButton(tea)
        exclusive_group.addButton(coffe)
        exclusive_group.setExclusive(True)

        drinks_layout = QtWidgets.QVBoxLayout()
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(tea)
        drinks_layout.addWidget(coffe)
        drinks.setLayout(drinks_layout)

        answers = QtWidgets.QGroupBox("Choose an answer")
        answer_a = QtWidgets.QRadioButton("A")
        answer_b = QtWidgets.QRadioButton("B")
        answer_c = QtWidgets.QRadioButton("C")

        answer_layout = QtWidgets.QVBoxLayout()
        answer_layout.addWidget(answer_a)
        answer_layout.addWidget(answer_b)
        answer_layout.addWidget(answer_c)
        answers.setLayout(answer_layout)

        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(oss)
        h_layout.addWidget(drinks)
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(answers)
        self.setLayout(layout)
