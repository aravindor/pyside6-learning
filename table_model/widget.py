from PySide6 import QtWidgets

from table_model.table_model import TableModel
from table_model.ui_widget import Ui_Form


class TableWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table demo")
        self.setupUi(self)
        self.model = TableModel()
        self.tableView.setModel(self.model)
