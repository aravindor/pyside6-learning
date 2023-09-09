from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QSettings

from settings.ui_settings import Ui_Form


class Settings(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Qt Settings test")
        self.color_list = [Qt.black, Qt.black, Qt.black, Qt.black, Qt.black, Qt.black, Qt.black, Qt.black, Qt.black, ]

        self.button_list = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                            self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9]
        #
        # for i, j in enumerate(self.button_list):
        #     j.clicked.connect(lambda: self.button_click(i))

        # def button_click(self, index):
        #     print(f"Clicked index {index}")
        #     color = QtWidgets.QColorDialog.getColor(self.color_list[index], self, "Choose color")
        #     if color.isValid():
        #         self.color_list[index] = color
        #         css = f"background-color : {color.name()}"
        #         print(css)
        #         self.button_list[index].setStyleSheet(css)
        self.pushButton.clicked.connect(self.button_1_click)
        self.pushButton_2.clicked.connect(self.button_2_click)
        self.pushButton_3.clicked.connect(self.button_3_click)
        self.pushButton_4.clicked.connect(self.button_4_click)
        self.pushButton_5.clicked.connect(self.button_5_click)
        self.pushButton_6.clicked.connect(self.button_6_click)
        self.pushButton_7.clicked.connect(self.button_7_click)
        self.pushButton_8.clicked.connect(self.button_8_click)
        self.pushButton_9.clicked.connect(self.button_9_click)

        self.pushButton_10.clicked.connect(self.load_color_button)
        self.pushButton_11.clicked.connect(self.save_button_color)

    def button_1_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[0], self, "Choose color")
        if color.isValid():
            self.color_list[0] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[0].setStyleSheet(css)

    def button_2_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[1], self, "Choose color")
        if color.isValid():
            self.color_list[1] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[1].setStyleSheet(css)

    def button_3_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[2], self, "Choose color")
        if color.isValid():
            self.color_list[2] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[2].setStyleSheet(css)

    def button_4_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[3], self, "Choose color")
        if color.isValid():
            self.color_list[3] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[3].setStyleSheet(css)

    def button_5_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[4], self, "Choose color")
        if color.isValid():
            self.color_list[4] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[4].setStyleSheet(css)

    def button_6_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[5], self, "Choose color")
        if color.isValid():
            self.color_list[5] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[5].setStyleSheet(css)

    def button_7_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[6], self, "Choose color")
        if color.isValid():
            self.color_list[6] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[6].setStyleSheet(css)

    def button_8_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[7], self, "Choose color")
        if color.isValid():
            self.color_list[7] = color
            css = f"background-color : {color.name()}"
            print(css)
            self.button_list[7].setStyleSheet(css)

    def button_9_click(self):
        color = QtWidgets.QColorDialog.getColor(self.color_list[8], self, "Choose color")
        if color.isValid():
            self.color_list[8] = color
            css = f"background-color : {color.name()}"
            self.button_list[8].setStyleSheet(css)

    def save_color(self, key, color):
        l_color = QtGui.QColor(color)
        red = l_color.red()
        green = l_color.green()
        blue = l_color.blue()
        settings = QSettings("my_settings", "color_checker")
        settings.beginGroup("button_color")
        settings.setValue(key + "r", red)
        settings.setValue(key + "g", green)
        settings.setValue(key + "b", blue)
        settings.endGroup()

    def load_color(self, key):
        settings = QSettings("my_settings", "color_checker")
        settings.beginGroup("button_color")
        red = settings.value(key + "r")
        green = settings.value(key + "g")
        blue = settings.value(key + "b")
        settings.endGroup()
        print(red, blue, green)
        return QtGui.QColor(red, blue, green)

    def set_loaded_color(self, key, index):
        color = self.load_color(key)
        self.color_list[index] = color
        css = f"background-color : {color.name()}"
        self.button_list[index].setStyleSheet(css)

    def save_button_color(self):
        for i, j in enumerate(self.color_list):
            self.save_color(f"button_{i + 1}", j)

    def load_color_button(self):
        for i, j in enumerate(self.button_list):
            self.set_loaded_color(f"button_{i + 1}", i)
