from typing import Union, Any

from PySide6 import QtCore
from PySide6.QtGui import QColor


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args):
        super(TableModel, self).__init__(*args)
        self.table = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "red"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "green"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "blue"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "yellow"]
        ]

    def data(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        if (role == QtCore.Qt.DisplayRole) or (role == QtCore.Qt.EditRole):
            return self.table[index.row()][index.column()]
        elif (role == QtCore.Qt.DecorationRole) and (index.column() == 6):
            return QColor(self.table[index.row()][index.column()])

    def rowCount(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex] = ...) -> int:
        if not index.isValid():
            return len(self.table)
        return 0

    def columnCount(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex] = ...) -> int:
        if not index.isValid():
            return len(self.table[0])
        return 0

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            if section == 0:
                return "First Name"
            if section == 1:
                return "Last Name"
            if section == 2:
                return "Age"
            if section == 3:
                return "Profession"
            if section == 4:
                return "Marital Status"
            if section == 5:
                return "Country"
            if section == 6:
                return "Favorite Color"
        return super().headerData(section, orientation, role)

    def setData(self, index, value, role):
        if not (role == QtCore.Qt.EditRole):
            return False
        self.table[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> QtCore.Qt.ItemFlag:
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable
