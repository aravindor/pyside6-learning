from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main window")
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(lambda: self.close())

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        window_menu = menu_bar.addMenu("Window")
        setting_menu = menu_bar.addMenu("Setting")
        help_menu = menu_bar.addMenu("Help")

        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)
        action1 = QAction("Some action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(lambda: self.statusBar().showMessage("Action 1 clicked", 3000))
        toolbar.addAction(action1)

        action2 = QAction(QIcon("img/start.png"), "Start", self)
        action2.setStatusTip("Status message for some action")
        action2.triggered.connect(lambda: print("Action 2 Clicked"))
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        self.setStatusBar(QStatusBar(self))
