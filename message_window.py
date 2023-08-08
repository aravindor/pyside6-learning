from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox


class MessageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message box example")
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.hard_button_clicked)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.critical_button_clicked)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.question_button_clicked)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.information_button_clicked)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.warning_button_clicked)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.about_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)

        self.setLayout(layout)

    def hard_button_clicked(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message title")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it ?")
        message.setIcon(QMessageBox.Icon.Critical)
        message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        message.setDefaultButton(QMessageBox.StandardButton.Ok)
        ret = message.exec()
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok Button clicked !!")
        else:
            print("Cancel Button clicked !!")

    def critical_button_clicked(self):
        ret = QMessageBox.critical(self, "Critical button", "Critical message here",
                                   QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Ok:
            print("Ok Button clicked !!")
        else:
            print("Cancel Button clicked !!")

    def question_button_clicked(self):
        ret = QMessageBox.question(self, "Question button", "Question message here",
                                   QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Ok:
            print("Ok Button clicked !!")
        else:
            print("Cancel Button clicked !!")

    def information_button_clicked(self):
        ret = QMessageBox.information(self, "Title", "Message body",
                                      QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Ok:
            print("Ok Button clicked !!")
        else:
            print("Cancel Button clicked !!")

    def warning_button_clicked(self):
        ret = QMessageBox.warning(self, "Title", "Message body",
                                  QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Ok:
            print("Ok Button clicked !!")
        else:
            print("Cancel Button clicked !!")

    def about_button_clicked(self):
        ret = QMessageBox.about(self, "Title", "Message body")

        if ret == QMessageBox.StandardButton.Ok:
            print("Ok Button clicked !!")
        else:
            print("Cancel Button clicked !!")
