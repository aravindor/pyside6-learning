# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plus_minus_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_PlusMinusForm(object):
    def setupUi(self, PlusMinusForm):
        if not PlusMinusForm.objectName():
            PlusMinusForm.setObjectName(u"PlusMinusForm")
        PlusMinusForm.resize(496, 300)
        self.horizontalLayout = QHBoxLayout(PlusMinusForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minus_button = QPushButton(PlusMinusForm)
        self.minus_button.setObjectName(u"minus_button")

        self.horizontalLayout.addWidget(self.minus_button)

        self.spin_box = QSpinBox(PlusMinusForm)
        self.spin_box.setObjectName(u"spin_box")

        self.horizontalLayout.addWidget(self.spin_box)

        self.plus_button = QPushButton(PlusMinusForm)
        self.plus_button.setObjectName(u"plus_button")

        self.horizontalLayout.addWidget(self.plus_button)


        self.retranslateUi(PlusMinusForm)

        QMetaObject.connectSlotsByName(PlusMinusForm)
    # setupUi

    def retranslateUi(self, PlusMinusForm):
        PlusMinusForm.setWindowTitle(QCoreApplication.translate("PlusMinusForm", u"Form", None))
        self.minus_button.setText(QCoreApplication.translate("PlusMinusForm", u"Minus", None))
        self.plus_button.setText(QCoreApplication.translate("PlusMinusForm", u"Plus", None))
    # retranslateUi

