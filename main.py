from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

from button_holder import ButtonHolder
from check_box import CheckBoxWidget
from edit_text_widget import EditTextWidget
from grid_layout import GridLayoutWidget
from line_edit_widget import LineEditWidget
from main_window import MainWindow
from message_window import MessageWidget
from rock_widget import RockWidget
from slider_holder import SliderHolder
from tab_layout import TabWidget

app = QApplication(sys.argv)
# button_holder = ButtonHolder()
# button_holder.show()
# widgetHolder = SliderHolder()
# widgetHolder.show()
# widgetHolder = RockWidget()
# widgetHolder.show()
# main_window = MainWindow()
# main_window.show()

# message_widget = MessageWidget()
# message_widget.show()

# line_edit_widget = LineEditWidget()
# line_edit_widget.show()
# text_edit_widget = EditTextWidget()
# text_edit_widget.show()
# grid_layout_widget = GridLayoutWidget()
# grid_layout_widget.show()
# checkbox_widget = CheckBoxWidget()
# checkbox_widget.show()

tab_widget = TabWidget()
tab_widget.show()
app.exec()
