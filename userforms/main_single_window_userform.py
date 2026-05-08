# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_single_window_userform.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_main_single_window(object):
    def setupUi(self, main_single_window):
        if not main_single_window.objectName():
            main_single_window.setObjectName(u"main_single_window")
        main_single_window.resize(682, 325)
        self.centralwidget = QWidget(main_single_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_pg_btn = QToolButton(self.centralwidget)
        self.home_pg_btn.setObjectName(u"home_pg_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_pg_btn.sizePolicy().hasHeightForWidth())
        self.home_pg_btn.setSizePolicy(sizePolicy)
        self.home_pg_btn.setStyleSheet(u"QToolButton {\n"
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
"    border: 2px solid rgba(92, 119, 245, 0.5); /* \u0411\u043e\u043b\u0435\u0435 \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"    background-color: rgba(92, 119, 245, 0.05);\n"
"}\n"
"\n"
"QTo"
                        "olButton:checked:pressed {\n"
"    background-color: rgba(92, 119, 245, 0.1);\n"
"}")
        self.home_pg_btn.setCheckable(True)
        self.home_pg_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.home_pg_btn)

        self.gearing_selection_btn = QToolButton(self.centralwidget)
        self.gearing_selection_btn.setObjectName(u"gearing_selection_btn")
        sizePolicy.setHeightForWidth(self.gearing_selection_btn.sizePolicy().hasHeightForWidth())
        self.gearing_selection_btn.setSizePolicy(sizePolicy)
        self.gearing_selection_btn.setStyleSheet(u"QToolButton {\n"
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
"    border: 2px solid rgba(64, 250, 64, 0.5); /* \u0411\u043e\u043b\u0435\u0435 \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"    background-color: rgba(64, 250, 64, 0.05);\n"
"}\n"
"\n"
"QTool"
                        "Button:checked:pressed {\n"
"    background-color: rgba(64, 250, 64, 0.1);\n"
"}")
        self.gearing_selection_btn.setCheckable(True)
        self.gearing_selection_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.gearing_selection_btn)

        self.gearing_calculation_btn = QToolButton(self.centralwidget)
        self.gearing_calculation_btn.setObjectName(u"gearing_calculation_btn")
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

        self.verticalLayout.addWidget(self.gearing_calculation_btn)

        self.gear_calculation_btn = QToolButton(self.centralwidget)
        self.gear_calculation_btn.setObjectName(u"gear_calculation_btn")
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

        self.verticalLayout.addWidget(self.gear_calculation_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QWidget#home_page {\n"
"    border: 2px solid rgba(92, 119, 245, 0.5); /* \u0442\u0451\u043c\u043d\u043e \u0441\u0438\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"}")
        self.verticalLayout_36 = QVBoxLayout(self.home_page)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.home_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gear_calculation_btn_2 = QToolButton(self.home_page)
        self.gear_calculation_btn_2.setObjectName(u"gear_calculation_btn_2")
        sizePolicy.setHeightForWidth(self.gear_calculation_btn_2.sizePolicy().hasHeightForWidth())
        self.gear_calculation_btn_2.setSizePolicy(sizePolicy)
        self.gear_calculation_btn_2.setStyleSheet(u"QToolButton {\n"
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
        self.gear_calculation_btn_2.setCheckable(True)
        self.gear_calculation_btn_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_25.addWidget(self.gear_calculation_btn_2, 2, 0, 1, 1)

        self.gearing_calculation_btn_2 = QToolButton(self.home_page)
        self.gearing_calculation_btn_2.setObjectName(u"gearing_calculation_btn_2")
        sizePolicy.setHeightForWidth(self.gearing_calculation_btn_2.sizePolicy().hasHeightForWidth())
        self.gearing_calculation_btn_2.setSizePolicy(sizePolicy)
        self.gearing_calculation_btn_2.setStyleSheet(u"QToolButton {\n"
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
        self.gearing_calculation_btn_2.setCheckable(True)
        self.gearing_calculation_btn_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_25.addWidget(self.gearing_calculation_btn_2, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.gearing_selection_btn_2 = QToolButton(self.home_page)
        self.gearing_selection_btn_2.setObjectName(u"gearing_selection_btn_2")
        sizePolicy.setHeightForWidth(self.gearing_selection_btn_2.sizePolicy().hasHeightForWidth())
        self.gearing_selection_btn_2.setSizePolicy(sizePolicy)
        self.gearing_selection_btn_2.setStyleSheet(u"QToolButton {\n"
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
"    border: 2px solid rgba(64, 250, 64, 0.5); /* \u0411\u043e\u043b\u0435\u0435 \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"    background-color: rgba(64, 250, 64, 0.05);\n"
"}\n"
"\n"
"QTool"
                        "Button:checked:pressed {\n"
"    background-color: rgba(64, 250, 64, 0.1);\n"
"}")
        self.gearing_selection_btn_2.setCheckable(True)
        self.gearing_selection_btn_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_25.addWidget(self.gearing_selection_btn_2, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_9, 3, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_25)


        self.verticalLayout_36.addLayout(self.verticalLayout_12)

        self.stackedWidget_2.addWidget(self.home_page)
        self.gearing_selection_page = QWidget()
        self.gearing_selection_page.setObjectName(u"gearing_selection_page")
        self.gearing_selection_page.setStyleSheet(u"QWidget#gearing_selection_page {\n"
"    border: 2px solid rgba(64, 250, 64, 0.5); /* \u0437\u0435\u043b\u0451\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"}")
        self.verticalLayout_44 = QVBoxLayout(self.gearing_selection_page)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_10 = QLabel(self.gearing_selection_page)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_10)

        self.stackedWidget_2.addWidget(self.gearing_selection_page)
        self.gearing_calculation_page = QWidget()
        self.gearing_calculation_page.setObjectName(u"gearing_calculation_page")
        self.gearing_calculation_page.setStyleSheet(u"QWidget#gearing_calculation_page {\n"
"    border: 2px solid rgba(243, 93, 93, 0.5); /* \u043a\u0440\u0430\u0441\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.gearing_calculation_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(self.gearing_calculation_page)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.stackedWidget_2.addWidget(self.gearing_calculation_page)
        self.gear_calculation_page = QWidget()
        self.gear_calculation_page.setObjectName(u"gear_calculation_page")
        self.gear_calculation_page.setStyleSheet(u"QWidget#gear_calculation_page {\n"
"    /*background-color: rgba(0, 188, 188, 0.1);*/\n"
"    border: 2px solid rgba(0, 188, 188, 0.5); /* \u0421\u0438\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    /*border-radius: 8px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.gear_calculation_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_12 = QLabel(self.gear_calculation_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_12)

        self.stackedWidget_2.addWidget(self.gear_calculation_page)

        self.horizontalLayout.addWidget(self.stackedWidget_2)

        main_single_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_single_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 682, 22))
        main_single_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_single_window)
        self.statusbar.setObjectName(u"statusbar")
        main_single_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_single_window)

        self.stackedWidget_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(main_single_window)
    # setupUi

    def retranslateUi(self, main_single_window):
        main_single_window.setWindowTitle(QCoreApplication.translate("main_single_window", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e (\u043e\u0434\u0438\u043d\u043e\u0447\u043d\u043e\u0435)", None))
        self.home_pg_btn.setText(QCoreApplication.translate("main_single_window", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.gearing_selection_btn.setText(QCoreApplication.translate("main_single_window", u"\u041f\u043e\u0434\u0431\u043e\u0440", None))
        self.gearing_calculation_btn.setText(QCoreApplication.translate("main_single_window", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.gear_calculation_btn.setText(QCoreApplication.translate("main_single_window", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
        self.label_8.setText(QCoreApplication.translate("main_single_window", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.gear_calculation_btn_2.setText(QCoreApplication.translate("main_single_window", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
        self.gearing_calculation_btn_2.setText(QCoreApplication.translate("main_single_window", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.gearing_selection_btn_2.setText(QCoreApplication.translate("main_single_window", u"\u041f\u043e\u0434\u0431\u043e\u0440", None))
        self.label_10.setText(QCoreApplication.translate("main_single_window", u"\u041f\u043e\u0434\u0431\u043e\u0440", None))
        self.label_11.setText(QCoreApplication.translate("main_single_window", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.label_12.setText(QCoreApplication.translate("main_single_window", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
    # retranslateUi

