# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculation_window_userform.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_Calculation_window(object):
    def setupUi(self, Calculation_window):
        if not Calculation_window.objectName():
            Calculation_window.setObjectName(u"Calculation_window")
        Calculation_window.resize(323, 200)
        self.centralwidget = QWidget(Calculation_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.first_spinbox = QDoubleSpinBox(self.centralwidget)
        self.first_spinbox.setObjectName(u"first_spinbox")
        self.first_spinbox.setDecimals(3)
        self.first_spinbox.setMinimum(-9999999999999.000000000000000)
        self.first_spinbox.setMaximum(9999999999999.000000000000000)

        self.verticalLayout.addWidget(self.first_spinbox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.multi_button = QToolButton(self.centralwidget)
        self.multi_button.setObjectName(u"multi_button")
        self.multi_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.multi_button)

        self.divide_button = QToolButton(self.centralwidget)
        self.divide_button.setObjectName(u"divide_button")
        self.divide_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.divide_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.second_spinbox = QDoubleSpinBox(self.centralwidget)
        self.second_spinbox.setObjectName(u"second_spinbox")
        self.second_spinbox.setDecimals(3)
        self.second_spinbox.setMinimum(-9999999999999.000000000000000)
        self.second_spinbox.setMaximum(9999999999999.000000000000000)

        self.verticalLayout.addWidget(self.second_spinbox)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.multiplication_spinbox = QDoubleSpinBox(self.centralwidget)
        self.multiplication_spinbox.setObjectName(u"multiplication_spinbox")
        self.multiplication_spinbox.setDecimals(3)
        self.multiplication_spinbox.setMinimum(-9999999999999.000000000000000)
        self.multiplication_spinbox.setMaximum(9999999999999.000000000000000)

        self.horizontalLayout_2.addWidget(self.multiplication_spinbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gearing_calculation_btn = QToolButton(self.centralwidget)
        self.gearing_calculation_btn.setObjectName(u"gearing_calculation_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gearing_calculation_btn.sizePolicy().hasHeightForWidth())
        self.gearing_calculation_btn.setSizePolicy(sizePolicy)
        self.gearing_calculation_btn.setStyleSheet(u"QToolButton {\n"
"    background-color: rgba(240, 240, 240, 1.0); /* \u0421\u0432\u0435\u0442\u043b\u043e\u2011\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #444444; /* \u0422\u0451\u043c\u043d\u043e\u2011\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border-radius: 8px;\n"
"    border: 2px solid #d0d0d0; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"/* \u0427\u0401\u0422\u041a\u0418\u0419 \u042d\u0424\u0424\u0415\u041a\u0422 \u041f\u0420\u0418 \u041d\u0410\u0412\u0415\u0414\u0415\u041d\u0418\u0418 \u041d\u0410 \u041d\u0415\u0410\u041a\u0422\u0418\u0412\u041d\u0423\u042e \u041a\u041d\u041e\u041f\u041a\u0423 */\n"
"QToolButton:hover {\n"
"    background-color: rgba(220, 220, 220, 1.0); /* \u0417\u0430\u043c\u0435\u0442\u043d\u043e \u0442\u0435\u043c\u043d\u0435\u0435 */\n"
"    border: 2px solid #b0b0b0; /* \u0422\u0435\u043c\u043d\u0435\u0435 \u0433\u0440\u0430\u043d\u0438\u0446\u0430 *"
                        "/\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: rgba(200, 200, 200, 1.0); /* \u0415\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid #909090;\n"
"    margin: 1px; /* \u041d\u0435\u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u0441\u0434\u0432\u0438\u0433 \u0434\u043b\u044f \u044d\u0444\u0444\u0435\u043a\u0442\u0430 \u043d\u0430\u0436\u0430\u0442\u0438\u044f */\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 CHECKED \u2014 \u043f\u0440\u0435\u0436\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 */\n"
"QToolButton:checked {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    border: 2px solid rgba(243, 93, 93, 0.5); /* \u0411\u043e\u043b\u0435\u0435 \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"    background-color: rgba(243, 93, 93, 0.05);\n"
"}\n"
"\n"
"QTool"
                        "Button:checked:pressed {\n"
"    background-color: rgba(243, 93, 93, 0.1);\n"
"}\n"
"\n"
"")
        self.gearing_calculation_btn.setCheckable(True)
        self.gearing_calculation_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.gearing_calculation_btn)

        Calculation_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Calculation_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 323, 22))
        Calculation_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Calculation_window)
        self.statusbar.setObjectName(u"statusbar")
        Calculation_window.setStatusBar(self.statusbar)

        self.retranslateUi(Calculation_window)

        QMetaObject.connectSlotsByName(Calculation_window)
    # setupUi

    def retranslateUi(self, Calculation_window):
        Calculation_window.setWindowTitle(QCoreApplication.translate("Calculation_window", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.multi_button.setText(QCoreApplication.translate("Calculation_window", u"x", None))
        self.divide_button.setText(QCoreApplication.translate("Calculation_window", u"/", None))
        self.label_2.setText(QCoreApplication.translate("Calculation_window", u"=", None))
        self.gearing_calculation_btn.setText(QCoreApplication.translate("Calculation_window", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
    # retranslateUi

