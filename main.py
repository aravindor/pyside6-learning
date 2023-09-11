from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

from button_holder import ButtonHolder
from check_box import CheckBoxWidget
from combo_box import ComboBoxWidget
from dialogs.file_dialog.file_picker import FilePicker
from dialogs.font_dialog.font_dialog_ui import FontDialog
from dialogs.ui.widget import SimpleInputDialog
from edit_text_widget import EditTextWidget
from grid_layout import GridLayoutWidget
from line_edit_widget import LineEditWidget
from list_widget.widget import ListWidget
# from main_window import MainWindow
from message_window import MessageWidget
from plus_minus_form import PlusMinusForm
from q_loader_as_q_object import UserInterFace
from qt_loader import get_qt_loader
from rock_widget import RockWidget
from settings.settings import Settings
from slider_holder import SliderHolder
from styles.widget import StyledWidget
from tab_layout import TabWidget
from table_model.widget import TableWidget
from ui.widget import Widget
from window.main_window import MainWindow

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

# tab_widget = TabWidget()
# tab_widget.show()

# combo_box_widget = ComboBoxWidget()
# combo_box_widget.show()
# qt_window = get_qt_loader()
# qt_window.show()
# window = UserInterFace()
# window.show()

# widget = Widget()
# widget.show()

# widget = PlusMinusForm()
# widget.show()

# window = MainWindow()
# window.show()

# dialog = SimpleInputDialog()
# dialog.show()
# widget = FilePicker()
# widget.show()
# widget = FontDialog()
# widget.show()
# app.setStyle("Fusion")
# widget = StyledWidget()
# widget.show()

# widget = Settings()
# widget.show()
# widget = ListWidget()
# widget.show()
widget = TableWidget()
widget.show()
app.exec()
