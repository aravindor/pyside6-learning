from PySide6.QtUiTools import QUiLoader


def get_qt_loader():
    loader = QUiLoader()
    window = loader.load("ui/widget.ui")
    window.setWindowTitle("Qt loader demo")
    return window
