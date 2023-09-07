# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DialogWidget(object):
    def setupUi(self, DialogWidget):
        if not DialogWidget.objectName():
            DialogWidget.setObjectName(u"DialogWidget")
        DialogWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DialogWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.provide_info_button = QPushButton(DialogWidget)
        self.provide_info_button.setObjectName(u"provide_info_button")

        self.verticalLayout.addWidget(self.provide_info_button)

        self.info_label = QLabel(DialogWidget)
        self.info_label.setObjectName(u"info_label")

        self.verticalLayout.addWidget(self.info_label)


        self.retranslateUi(DialogWidget)

        QMetaObject.connectSlotsByName(DialogWidget)
    # setupUi

    def retranslateUi(self, DialogWidget):
        DialogWidget.setWindowTitle(QCoreApplication.translate("DialogWidget", u"Form", None))
        self.provide_info_button.setText(QCoreApplication.translate("DialogWidget", u"Provide info", None))
        self.info_label.setText(QCoreApplication.translate("DialogWidget", u"Some text", None))
    # retranslateUi

