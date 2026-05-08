# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'added_calculation_window_userform.ui'
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

class Ui_Added_window(object):
    def setupUi(self, Added_window):
        if not Added_window.objectName():
            Added_window.setObjectName(u"Added_window")
        Added_window.resize(383, 172)
        self.centralwidget = QWidget(Added_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.degree_spinbox = QDoubleSpinBox(self.centralwidget)
        self.degree_spinbox.setObjectName(u"degree_spinbox")
        self.degree_spinbox.setDecimals(3)
        self.degree_spinbox.setMinimum(-9999999999999.000000000000000)
        self.degree_spinbox.setMaximum(9999999999999.000000000000000)

        self.horizontalLayout.addWidget(self.degree_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.main_number_spinbox = QDoubleSpinBox(self.centralwidget)
        self.main_number_spinbox.setObjectName(u"main_number_spinbox")
        self.main_number_spinbox.setDecimals(3)
        self.main_number_spinbox.setMinimum(-9999999999999.000000000000000)
        self.main_number_spinbox.setMaximum(9999999999999.000000000000000)

        self.horizontalLayout_2.addWidget(self.main_number_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.result_spinbox = QDoubleSpinBox(self.centralwidget)
        self.result_spinbox.setObjectName(u"result_spinbox")
        self.result_spinbox.setDecimals(3)
        self.result_spinbox.setMinimum(-9999999999999.000000000000000)
        self.result_spinbox.setMaximum(9999999999999.000000000000000)

        self.horizontalLayout_3.addWidget(self.result_spinbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.gear_calculation_btn = QToolButton(self.centralwidget)
        self.gear_calculation_btn.setObjectName(u"gear_calculation_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gear_calculation_btn.sizePolicy().hasHeightForWidth())
        self.gear_calculation_btn.setSizePolicy(sizePolicy)
        self.gear_calculation_btn.setStyleSheet(u"QToolButton {\n"
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
"    border: 2px solid rgba(0, 188, 188, 0.5); /* \u0411\u043e\u043b\u0435\u0435 \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"    background-color: rgba(0, 188, 188, 0.05);\n"
"/*    border: 2p"
                        "x solid rgba(0, 150, 150, 0.9); /* \u0422\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QToolButton:checked:pressed {\n"
"    background-color: rgba(0, 188, 188, 0.1);\n"
"}\n"
"")
        self.gear_calculation_btn.setCheckable(True)
        self.gear_calculation_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.gear_calculation_btn)

        Added_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Added_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 383, 22))
        Added_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Added_window)
        self.statusbar.setObjectName(u"statusbar")
        Added_window.setStatusBar(self.statusbar)

        self.retranslateUi(Added_window)

        QMetaObject.connectSlotsByName(Added_window)
    # setupUi

    def retranslateUi(self, Added_window):
        Added_window.setWindowTitle(QCoreApplication.translate("Added_window", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
        self.label_3.setText(QCoreApplication.translate("Added_window", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Added_window", u"\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Added_window", u"=", None))
        self.gear_calculation_btn.setText(QCoreApplication.translate("Added_window", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
    # retranslateUi

