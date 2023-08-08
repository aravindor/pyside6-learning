from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

from button_holder import ButtonHolder
from main_window import MainWindow
from message_window import MessageWidget
from rock_widget import RockWidget
from slider_holder import SliderHolder

app = QApplication(sys.argv)
# button_holder = ButtonHolder()
# button_holder.show()
# widgetHolder = SliderHolder()
# widgetHolder.show()
# widgetHolder = RockWidget()
# widgetHolder.show()
# main_window = MainWindow()
# main_window.show()

message_widget = MessageWidget()
message_widget.show()
app.exec()
