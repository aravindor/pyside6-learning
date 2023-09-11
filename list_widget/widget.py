from PySide6 import QtWidgets

from list_widget.ui_widget import Ui_Form


class ListWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.items = []
        self.setWindowTitle("List widget example")
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_item)
        self.remove_button.clicked.connect(self.remove_item)

    def add_item(self):
        text = self.line_edit.text()
        self.items.append(text)
        self.listWidget.addItem(QtWidgets.QListWidgetItem(text))

    def remove_item(self):
        current_item = self.listWidget.currentItem()
        index = self.items.index(current_item.text())
        if current_item is not None:
            self.listWidget.takeItem(index)
            self.items.remove(current_item.text())
