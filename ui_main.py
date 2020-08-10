# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main - 002.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import Images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 540)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMinimumSize(QSize(0, 70))
        self.Top_Bar.setMaximumSize(QSize(16777215, 70))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(250, 70))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_toggle)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.label_8.setPixmap(QPixmap(u":/logo/Images/EST Logo.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_8)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 40))
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(250, 580))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(0, 0))
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_hpc = QPushButton(self.frame_top_menus)
        self.Btn_hpc.setObjectName(u"Btn_hpc")
        self.Btn_hpc.setEnabled(True)
        self.Btn_hpc.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(10)
        self.Btn_hpc.setFont(font)
        self.Btn_hpc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_hpc)

        self.frame_hpc = QFrame(self.frame_top_menus)
        self.frame_hpc.setObjectName(u"frame_hpc")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_hpc.sizePolicy().hasHeightForWidth())
        self.frame_hpc.setSizePolicy(sizePolicy)
        self.frame_hpc.setMinimumSize(QSize(0, 0))
        self.frame_hpc.setMaximumSize(QSize(16777215, 0))
        self.frame_hpc.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_hpc.setFrameShape(QFrame.StyledPanel)
        self.frame_hpc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_hpc)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Btn_hpc_main = QPushButton(self.frame_hpc)
        self.Btn_hpc_main.setObjectName(u"Btn_hpc_main")
        self.Btn_hpc_main.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_main.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_main.setSizePolicy(sizePolicy1)
        self.Btn_hpc_main.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        self.Btn_hpc_main.setFont(font1)
        self.Btn_hpc_main.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_main.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.Btn_hpc_main)

        self.Btn_hpc_process = QPushButton(self.frame_hpc)
        self.Btn_hpc_process.setObjectName(u"Btn_hpc_process")
        self.Btn_hpc_process.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_process.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_process.setSizePolicy(sizePolicy1)
        self.Btn_hpc_process.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_process.setFont(font1)
        self.Btn_hpc_process.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.Btn_hpc_process)

        self.Btn_hpc_mat = QPushButton(self.frame_hpc)
        self.Btn_hpc_mat.setObjectName(u"Btn_hpc_mat")
        self.Btn_hpc_mat.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_mat.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_mat.setSizePolicy(sizePolicy1)
        self.Btn_hpc_mat.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_mat.setFont(font1)
        self.Btn_hpc_mat.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_mat.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.Btn_hpc_mat)

        self.Btn_hpc_qc = QPushButton(self.frame_hpc)
        self.Btn_hpc_qc.setObjectName(u"Btn_hpc_qc")
        self.Btn_hpc_qc.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_qc.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_qc.setSizePolicy(sizePolicy1)
        self.Btn_hpc_qc.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_qc.setFont(font1)
        self.Btn_hpc_qc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_qc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.Btn_hpc_qc)

        self.Btn_hpc_manu = QPushButton(self.frame_hpc)
        self.Btn_hpc_manu.setObjectName(u"Btn_hpc_manu")
        self.Btn_hpc_manu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_manu.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_manu.setSizePolicy(sizePolicy1)
        self.Btn_hpc_manu.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_manu.setFont(font1)
        self.Btn_hpc_manu.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_manu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.Btn_hpc_manu)

        self.Btn_hpc_pack = QPushButton(self.frame_hpc)
        self.Btn_hpc_pack.setObjectName(u"Btn_hpc_pack")
        self.Btn_hpc_pack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_pack.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_pack.setSizePolicy(sizePolicy1)
        self.Btn_hpc_pack.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_pack.setFont(font1)
        self.Btn_hpc_pack.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_pack.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.Btn_hpc_pack)


        self.verticalLayout_2.addWidget(self.frame_hpc)

        self.Btn_spc = QPushButton(self.frame_top_menus)
        self.Btn_spc.setObjectName(u"Btn_spc")
        self.Btn_spc.setMinimumSize(QSize(0, 40))
        self.Btn_spc.setFont(font)
        self.Btn_spc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_spc)

        self.frame_spc = QFrame(self.frame_top_menus)
        self.frame_spc.setObjectName(u"frame_spc")
        sizePolicy.setHeightForWidth(self.frame_spc.sizePolicy().hasHeightForWidth())
        self.frame_spc.setSizePolicy(sizePolicy)
        self.frame_spc.setMinimumSize(QSize(0, 0))
        self.frame_spc.setMaximumSize(QSize(16777215, 0))
        self.frame_spc.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_spc.setFrameShape(QFrame.StyledPanel)
        self.frame_spc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_spc)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Btn_spc_main = QPushButton(self.frame_spc)
        self.Btn_spc_main.setObjectName(u"Btn_spc_main")
        self.Btn_spc_main.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_spc_main.sizePolicy().hasHeightForWidth())
        self.Btn_spc_main.setSizePolicy(sizePolicy1)
        self.Btn_spc_main.setMinimumSize(QSize(0, 0))
        self.Btn_spc_main.setFont(font1)
        self.Btn_spc_main.setLayoutDirection(Qt.LeftToRight)
        self.Btn_spc_main.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_spc_main)

        self.Btn_spc_process = QPushButton(self.frame_spc)
        self.Btn_spc_process.setObjectName(u"Btn_spc_process")
        self.Btn_spc_process.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_spc_process.sizePolicy().hasHeightForWidth())
        self.Btn_spc_process.setSizePolicy(sizePolicy1)
        self.Btn_spc_process.setMinimumSize(QSize(0, 0))
        self.Btn_spc_process.setFont(font1)
        self.Btn_spc_process.setLayoutDirection(Qt.LeftToRight)
        self.Btn_spc_process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_spc_process)

        self.Btn_spc_mat = QPushButton(self.frame_spc)
        self.Btn_spc_mat.setObjectName(u"Btn_spc_mat")
        self.Btn_spc_mat.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_spc_mat.sizePolicy().hasHeightForWidth())
        self.Btn_spc_mat.setSizePolicy(sizePolicy1)
        self.Btn_spc_mat.setMinimumSize(QSize(0, 0))
        self.Btn_spc_mat.setFont(font1)
        self.Btn_spc_mat.setLayoutDirection(Qt.LeftToRight)
        self.Btn_spc_mat.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_spc_mat)

        self.Btn_spc_qc = QPushButton(self.frame_spc)
        self.Btn_spc_qc.setObjectName(u"Btn_spc_qc")
        self.Btn_spc_qc.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_spc_qc.sizePolicy().hasHeightForWidth())
        self.Btn_spc_qc.setSizePolicy(sizePolicy1)
        self.Btn_spc_qc.setMinimumSize(QSize(0, 0))
        self.Btn_spc_qc.setFont(font1)
        self.Btn_spc_qc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_spc_qc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_spc_qc)

        self.Btn_spc_manu = QPushButton(self.frame_spc)
        self.Btn_spc_manu.setObjectName(u"Btn_spc_manu")
        self.Btn_spc_manu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_spc_manu.sizePolicy().hasHeightForWidth())
        self.Btn_spc_manu.setSizePolicy(sizePolicy1)
        self.Btn_spc_manu.setMinimumSize(QSize(0, 0))
        self.Btn_spc_manu.setFont(font1)
        self.Btn_spc_manu.setLayoutDirection(Qt.LeftToRight)
        self.Btn_spc_manu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_spc_manu)

        self.Btn_spc_pack = QPushButton(self.frame_spc)
        self.Btn_spc_pack.setObjectName(u"Btn_spc_pack")
        self.Btn_spc_pack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_spc_pack.sizePolicy().hasHeightForWidth())
        self.Btn_spc_pack.setSizePolicy(sizePolicy1)
        self.Btn_spc_pack.setMinimumSize(QSize(0, 0))
        self.Btn_spc_pack.setFont(font1)
        self.Btn_spc_pack.setLayoutDirection(Qt.LeftToRight)
        self.Btn_spc_pack.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_spc_pack)


        self.verticalLayout_2.addWidget(self.frame_spc)

        self.Btn_dpc = QPushButton(self.frame_top_menus)
        self.Btn_dpc.setObjectName(u"Btn_dpc")
        self.Btn_dpc.setMinimumSize(QSize(0, 40))
        self.Btn_dpc.setFont(font)
        self.Btn_dpc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_dpc)

        self.frame_dpc = QFrame(self.frame_top_menus)
        self.frame_dpc.setObjectName(u"frame_dpc")
        sizePolicy.setHeightForWidth(self.frame_dpc.sizePolicy().hasHeightForWidth())
        self.frame_dpc.setSizePolicy(sizePolicy)
        self.frame_dpc.setMinimumSize(QSize(0, 0))
        self.frame_dpc.setMaximumSize(QSize(16777215, 0))
        self.frame_dpc.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_dpc.setFrameShape(QFrame.StyledPanel)
        self.frame_dpc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_dpc)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Btn_dpc_main = QPushButton(self.frame_dpc)
        self.Btn_dpc_main.setObjectName(u"Btn_dpc_main")
        self.Btn_dpc_main.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_dpc_main.sizePolicy().hasHeightForWidth())
        self.Btn_dpc_main.setSizePolicy(sizePolicy1)
        self.Btn_dpc_main.setMinimumSize(QSize(0, 0))
        self.Btn_dpc_main.setFont(font1)
        self.Btn_dpc_main.setLayoutDirection(Qt.LeftToRight)
        self.Btn_dpc_main.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_dpc_main)

        self.Btn_dpc_process = QPushButton(self.frame_dpc)
        self.Btn_dpc_process.setObjectName(u"Btn_dpc_process")
        self.Btn_dpc_process.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_dpc_process.sizePolicy().hasHeightForWidth())
        self.Btn_dpc_process.setSizePolicy(sizePolicy1)
        self.Btn_dpc_process.setMinimumSize(QSize(0, 0))
        self.Btn_dpc_process.setFont(font1)
        self.Btn_dpc_process.setLayoutDirection(Qt.LeftToRight)
        self.Btn_dpc_process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_dpc_process)

        self.Btn_dpc_mat = QPushButton(self.frame_dpc)
        self.Btn_dpc_mat.setObjectName(u"Btn_dpc_mat")
        self.Btn_dpc_mat.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_dpc_mat.sizePolicy().hasHeightForWidth())
        self.Btn_dpc_mat.setSizePolicy(sizePolicy1)
        self.Btn_dpc_mat.setMinimumSize(QSize(0, 0))
        self.Btn_dpc_mat.setFont(font1)
        self.Btn_dpc_mat.setLayoutDirection(Qt.LeftToRight)
        self.Btn_dpc_mat.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_dpc_mat)

        self.Btn_dpc_qc = QPushButton(self.frame_dpc)
        self.Btn_dpc_qc.setObjectName(u"Btn_dpc_qc")
        self.Btn_dpc_qc.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_dpc_qc.sizePolicy().hasHeightForWidth())
        self.Btn_dpc_qc.setSizePolicy(sizePolicy1)
        self.Btn_dpc_qc.setMinimumSize(QSize(0, 0))
        self.Btn_dpc_qc.setFont(font1)
        self.Btn_dpc_qc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_dpc_qc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_dpc_qc)

        self.Btn_dpc_manu = QPushButton(self.frame_dpc)
        self.Btn_dpc_manu.setObjectName(u"Btn_dpc_manu")
        self.Btn_dpc_manu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_dpc_manu.sizePolicy().hasHeightForWidth())
        self.Btn_dpc_manu.setSizePolicy(sizePolicy1)
        self.Btn_dpc_manu.setMinimumSize(QSize(0, 0))
        self.Btn_dpc_manu.setFont(font1)
        self.Btn_dpc_manu.setLayoutDirection(Qt.LeftToRight)
        self.Btn_dpc_manu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_dpc_manu)

        self.Btn_dpc_pack = QPushButton(self.frame_dpc)
        self.Btn_dpc_pack.setObjectName(u"Btn_dpc_pack")
        self.Btn_dpc_pack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_dpc_pack.sizePolicy().hasHeightForWidth())
        self.Btn_dpc_pack.setSizePolicy(sizePolicy1)
        self.Btn_dpc_pack.setMinimumSize(QSize(0, 0))
        self.Btn_dpc_pack.setFont(font1)
        self.Btn_dpc_pack.setLayoutDirection(Qt.LeftToRight)
        self.Btn_dpc_pack.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_dpc_pack)


        self.verticalLayout_2.addWidget(self.frame_dpc)

        self.Btn_ssc = QPushButton(self.frame_top_menus)
        self.Btn_ssc.setObjectName(u"Btn_ssc")
        self.Btn_ssc.setMinimumSize(QSize(0, 40))
        self.Btn_ssc.setFont(font)
        self.Btn_ssc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_ssc)

        self.frame_ssc = QFrame(self.frame_top_menus)
        self.frame_ssc.setObjectName(u"frame_ssc")
        sizePolicy.setHeightForWidth(self.frame_ssc.sizePolicy().hasHeightForWidth())
        self.frame_ssc.setSizePolicy(sizePolicy)
        self.frame_ssc.setMinimumSize(QSize(0, 0))
        self.frame_ssc.setMaximumSize(QSize(16777215, 0))
        self.frame_ssc.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_ssc.setFrameShape(QFrame.StyledPanel)
        self.frame_ssc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_ssc)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Btn_ssc_main = QPushButton(self.frame_ssc)
        self.Btn_ssc_main.setObjectName(u"Btn_ssc_main")
        self.Btn_ssc_main.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_ssc_main.sizePolicy().hasHeightForWidth())
        self.Btn_ssc_main.setSizePolicy(sizePolicy1)
        self.Btn_ssc_main.setMinimumSize(QSize(0, 0))
        self.Btn_ssc_main.setFont(font1)
        self.Btn_ssc_main.setLayoutDirection(Qt.LeftToRight)
        self.Btn_ssc_main.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_ssc_main)

        self.Btn_ssc_process = QPushButton(self.frame_ssc)
        self.Btn_ssc_process.setObjectName(u"Btn_ssc_process")
        self.Btn_ssc_process.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_ssc_process.sizePolicy().hasHeightForWidth())
        self.Btn_ssc_process.setSizePolicy(sizePolicy1)
        self.Btn_ssc_process.setMinimumSize(QSize(0, 0))
        self.Btn_ssc_process.setFont(font1)
        self.Btn_ssc_process.setLayoutDirection(Qt.LeftToRight)
        self.Btn_ssc_process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_ssc_process)

        self.Btn_ssc_mat = QPushButton(self.frame_ssc)
        self.Btn_ssc_mat.setObjectName(u"Btn_ssc_mat")
        self.Btn_ssc_mat.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_ssc_mat.sizePolicy().hasHeightForWidth())
        self.Btn_ssc_mat.setSizePolicy(sizePolicy1)
        self.Btn_ssc_mat.setMinimumSize(QSize(0, 0))
        self.Btn_ssc_mat.setFont(font1)
        self.Btn_ssc_mat.setLayoutDirection(Qt.LeftToRight)
        self.Btn_ssc_mat.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_ssc_mat)

        self.Btn_ssc_qc = QPushButton(self.frame_ssc)
        self.Btn_ssc_qc.setObjectName(u"Btn_ssc_qc")
        self.Btn_ssc_qc.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_ssc_qc.sizePolicy().hasHeightForWidth())
        self.Btn_ssc_qc.setSizePolicy(sizePolicy1)
        self.Btn_ssc_qc.setMinimumSize(QSize(0, 0))
        self.Btn_ssc_qc.setFont(font1)
        self.Btn_ssc_qc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_ssc_qc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_ssc_qc)

        self.Btn_ssc_manu = QPushButton(self.frame_ssc)
        self.Btn_ssc_manu.setObjectName(u"Btn_ssc_manu")
        self.Btn_ssc_manu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_ssc_manu.sizePolicy().hasHeightForWidth())
        self.Btn_ssc_manu.setSizePolicy(sizePolicy1)
        self.Btn_ssc_manu.setMinimumSize(QSize(0, 0))
        self.Btn_ssc_manu.setFont(font1)
        self.Btn_ssc_manu.setLayoutDirection(Qt.LeftToRight)
        self.Btn_ssc_manu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_ssc_manu)

        self.Btn_ssc_pack = QPushButton(self.frame_ssc)
        self.Btn_ssc_pack.setObjectName(u"Btn_ssc_pack")
        self.Btn_ssc_pack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_ssc_pack.sizePolicy().hasHeightForWidth())
        self.Btn_ssc_pack.setSizePolicy(sizePolicy1)
        self.Btn_ssc_pack.setMinimumSize(QSize(0, 0))
        self.Btn_ssc_pack.setFont(font1)
        self.Btn_ssc_pack.setLayoutDirection(Qt.LeftToRight)
        self.Btn_ssc_pack.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_ssc_pack)


        self.verticalLayout_2.addWidget(self.frame_ssc, 0, Qt.AlignTop)

        self.Btn_alc = QPushButton(self.frame_top_menus)
        self.Btn_alc.setObjectName(u"Btn_alc")
        self.Btn_alc.setMinimumSize(QSize(0, 40))
        self.Btn_alc.setFont(font)
        self.Btn_alc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_alc)

        self.frame_alc = QFrame(self.frame_top_menus)
        self.frame_alc.setObjectName(u"frame_alc")
        sizePolicy.setHeightForWidth(self.frame_alc.sizePolicy().hasHeightForWidth())
        self.frame_alc.setSizePolicy(sizePolicy)
        self.frame_alc.setMinimumSize(QSize(0, 0))
        self.frame_alc.setMaximumSize(QSize(16777215, 0))
        self.frame_alc.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_alc.setFrameShape(QFrame.StyledPanel)
        self.frame_alc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_alc)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Btn_alc_main = QPushButton(self.frame_alc)
        self.Btn_alc_main.setObjectName(u"Btn_alc_main")
        self.Btn_alc_main.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_alc_main.sizePolicy().hasHeightForWidth())
        self.Btn_alc_main.setSizePolicy(sizePolicy1)
        self.Btn_alc_main.setMinimumSize(QSize(0, 0))
        self.Btn_alc_main.setFont(font1)
        self.Btn_alc_main.setLayoutDirection(Qt.LeftToRight)
        self.Btn_alc_main.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_alc_main)

        self.Btn_alc_process = QPushButton(self.frame_alc)
        self.Btn_alc_process.setObjectName(u"Btn_alc_process")
        self.Btn_alc_process.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_alc_process.sizePolicy().hasHeightForWidth())
        self.Btn_alc_process.setSizePolicy(sizePolicy1)
        self.Btn_alc_process.setMinimumSize(QSize(0, 0))
        self.Btn_alc_process.setFont(font1)
        self.Btn_alc_process.setLayoutDirection(Qt.LeftToRight)
        self.Btn_alc_process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_alc_process)

        self.Btn_alc_mat = QPushButton(self.frame_alc)
        self.Btn_alc_mat.setObjectName(u"Btn_alc_mat")
        self.Btn_alc_mat.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_alc_mat.sizePolicy().hasHeightForWidth())
        self.Btn_alc_mat.setSizePolicy(sizePolicy1)
        self.Btn_alc_mat.setMinimumSize(QSize(0, 0))
        self.Btn_alc_mat.setFont(font1)
        self.Btn_alc_mat.setLayoutDirection(Qt.LeftToRight)
        self.Btn_alc_mat.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_alc_mat)

        self.Btn_alc_qc = QPushButton(self.frame_alc)
        self.Btn_alc_qc.setObjectName(u"Btn_alc_qc")
        self.Btn_alc_qc.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_alc_qc.sizePolicy().hasHeightForWidth())
        self.Btn_alc_qc.setSizePolicy(sizePolicy1)
        self.Btn_alc_qc.setMinimumSize(QSize(0, 0))
        self.Btn_alc_qc.setFont(font1)
        self.Btn_alc_qc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_alc_qc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_alc_qc)

        self.Btn_alc_manu = QPushButton(self.frame_alc)
        self.Btn_alc_manu.setObjectName(u"Btn_alc_manu")
        self.Btn_alc_manu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_alc_manu.sizePolicy().hasHeightForWidth())
        self.Btn_alc_manu.setSizePolicy(sizePolicy1)
        self.Btn_alc_manu.setMinimumSize(QSize(0, 0))
        self.Btn_alc_manu.setFont(font1)
        self.Btn_alc_manu.setLayoutDirection(Qt.LeftToRight)
        self.Btn_alc_manu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_alc_manu)

        self.Btn_alc_pack = QPushButton(self.frame_alc)
        self.Btn_alc_pack.setObjectName(u"Btn_alc_pack")
        self.Btn_alc_pack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_alc_pack.sizePolicy().hasHeightForWidth())
        self.Btn_alc_pack.setSizePolicy(sizePolicy1)
        self.Btn_alc_pack.setMinimumSize(QSize(0, 0))
        self.Btn_alc_pack.setFont(font1)
        self.Btn_alc_pack.setLayoutDirection(Qt.LeftToRight)
        self.Btn_alc_pack.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_alc_pack)


        self.verticalLayout_2.addWidget(self.frame_alc)

        self.Btn_cmt = QPushButton(self.frame_top_menus)
        self.Btn_cmt.setObjectName(u"Btn_cmt")
        self.Btn_cmt.setMinimumSize(QSize(0, 40))
        self.Btn_cmt.setFont(font)
        self.Btn_cmt.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_cmt)

        self.frame_cmt = QFrame(self.frame_top_menus)
        self.frame_cmt.setObjectName(u"frame_cmt")
        sizePolicy.setHeightForWidth(self.frame_cmt.sizePolicy().hasHeightForWidth())
        self.frame_cmt.setSizePolicy(sizePolicy)
        self.frame_cmt.setMinimumSize(QSize(0, 0))
        self.frame_cmt.setMaximumSize(QSize(16777215, 0))
        self.frame_cmt.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_cmt.setFrameShape(QFrame.StyledPanel)
        self.frame_cmt.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_cmt)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Btn_cmt_main = QPushButton(self.frame_cmt)
        self.Btn_cmt_main.setObjectName(u"Btn_cmt_main")
        self.Btn_cmt_main.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_cmt_main.sizePolicy().hasHeightForWidth())
        self.Btn_cmt_main.setSizePolicy(sizePolicy1)
        self.Btn_cmt_main.setMinimumSize(QSize(0, 0))
        self.Btn_cmt_main.setFont(font1)
        self.Btn_cmt_main.setLayoutDirection(Qt.LeftToRight)
        self.Btn_cmt_main.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_cmt_main)

        self.Btn_cmt_process = QPushButton(self.frame_cmt)
        self.Btn_cmt_process.setObjectName(u"Btn_cmt_process")
        self.Btn_cmt_process.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_cmt_process.sizePolicy().hasHeightForWidth())
        self.Btn_cmt_process.setSizePolicy(sizePolicy1)
        self.Btn_cmt_process.setMinimumSize(QSize(0, 0))
        self.Btn_cmt_process.setFont(font1)
        self.Btn_cmt_process.setLayoutDirection(Qt.LeftToRight)
        self.Btn_cmt_process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_cmt_process)

        self.Btn_cmt_mat = QPushButton(self.frame_cmt)
        self.Btn_cmt_mat.setObjectName(u"Btn_cmt_mat")
        self.Btn_cmt_mat.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_cmt_mat.sizePolicy().hasHeightForWidth())
        self.Btn_cmt_mat.setSizePolicy(sizePolicy1)
        self.Btn_cmt_mat.setMinimumSize(QSize(0, 0))
        self.Btn_cmt_mat.setFont(font1)
        self.Btn_cmt_mat.setLayoutDirection(Qt.LeftToRight)
        self.Btn_cmt_mat.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_cmt_mat)

        self.Btn_cmt_qc = QPushButton(self.frame_cmt)
        self.Btn_cmt_qc.setObjectName(u"Btn_cmt_qc")
        self.Btn_cmt_qc.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_cmt_qc.sizePolicy().hasHeightForWidth())
        self.Btn_cmt_qc.setSizePolicy(sizePolicy1)
        self.Btn_cmt_qc.setMinimumSize(QSize(0, 0))
        self.Btn_cmt_qc.setFont(font1)
        self.Btn_cmt_qc.setLayoutDirection(Qt.LeftToRight)
        self.Btn_cmt_qc.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_cmt_qc)

        self.Btn_cmt_manu = QPushButton(self.frame_cmt)
        self.Btn_cmt_manu.setObjectName(u"Btn_cmt_manu")
        self.Btn_cmt_manu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_cmt_manu.sizePolicy().hasHeightForWidth())
        self.Btn_cmt_manu.setSizePolicy(sizePolicy1)
        self.Btn_cmt_manu.setMinimumSize(QSize(0, 0))
        self.Btn_cmt_manu.setFont(font1)
        self.Btn_cmt_manu.setLayoutDirection(Qt.LeftToRight)
        self.Btn_cmt_manu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_cmt_manu)

        self.Btn_cmt_pack = QPushButton(self.frame_cmt)
        self.Btn_cmt_pack.setObjectName(u"Btn_cmt_pack")
        self.Btn_cmt_pack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_cmt_pack.sizePolicy().hasHeightForWidth())
        self.Btn_cmt_pack.setSizePolicy(sizePolicy1)
        self.Btn_cmt_pack.setMinimumSize(QSize(0, 0))
        self.Btn_cmt_pack.setFont(font1)
        self.Btn_cmt_pack.setLayoutDirection(Qt.LeftToRight)
        self.Btn_cmt_pack.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_cmt_pack)


        self.verticalLayout_2.addWidget(self.frame_cmt)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(1)
        self.page_hpc_main = QWidget()
        self.page_hpc_main.setObjectName(u"page_hpc_main")
        self.verticalLayout_18 = QVBoxLayout(self.page_hpc_main)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_9 = QLabel(self.page_hpc_main)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        palette = QPalette()
        brush = QBrush(QColor(45, 45, 45, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_9.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(24)
        self.label_9.setFont(font2)

        self.verticalLayout_15.addWidget(self.label_9)

        self.frame_6 = QFrame(self.page_hpc_main)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMaximumSize(QSize(16777215, 25))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.label_10.setPalette(palette1)
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"selection-color: rgb(255, 255, 255);")
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_7 = QLineEdit(self.frame_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMinimumSize(QSize(350, 0))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_7.setSizeIncrement(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_7.setPalette(palette2)
        font4 = QFont()
        font4.setFamily(u"Helvetica")
        font4.setPointSize(14)
        self.lineEdit_7.setFont(font4)
        self.lineEdit_7.setStyleSheet(u"text-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.lineEdit_7.setFrame(True)
        self.lineEdit_7.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(16777215, 25))
        self.label_11.setBaseSize(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_11.setPalette(palette3)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"")
        self.label_11.setWordWrap(False)
        self.label_11.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_8 = QLineEdit(self.frame_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy3.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy3)
        self.lineEdit_8.setMinimumSize(QSize(200, 0))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_8.setSizeIncrement(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_8.setPalette(palette4)
        self.lineEdit_8.setFont(font4)
        self.lineEdit_8.setFrame(True)
        self.lineEdit_8.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMaximumSize(QSize(16777215, 25))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_12.setPalette(palette5)
        self.label_12.setFont(font3)
        self.label_12.setWordWrap(False)
        self.label_12.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_9 = QLineEdit(self.frame_6)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy3.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy3)
        self.lineEdit_9.setMinimumSize(QSize(200, 0))
        self.lineEdit_9.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_9.setSizeIncrement(QSize(0, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_9.setPalette(palette6)
        self.lineEdit_9.setFont(font4)
        self.lineEdit_9.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.lineEdit_9.setFrame(True)
        self.lineEdit_9.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMaximumSize(QSize(16777215, 25))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_13.setPalette(palette7)
        self.label_13.setFont(font3)
        self.label_13.setWordWrap(False)
        self.label_13.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_10 = QLineEdit(self.frame_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy3.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy3)
        self.lineEdit_10.setMinimumSize(QSize(200, 0))
        self.lineEdit_10.setMaximumSize(QSize(16777215, 16777215))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_10.setPalette(palette8)
        self.lineEdit_10.setFont(font4)
        self.lineEdit_10.setFrame(True)
        self.lineEdit_10.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMaximumSize(QSize(16777215, 25))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_14.setPalette(palette9)
        self.label_14.setFont(font3)
        self.label_14.setWordWrap(False)
        self.label_14.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_11 = QLineEdit(self.frame_6)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy3.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy3)
        self.lineEdit_11.setMinimumSize(QSize(200, 0))
        self.lineEdit_11.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_11.setSizeIncrement(QSize(0, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_11.setPalette(palette10)
        self.lineEdit_11.setFont(font4)
        self.lineEdit_11.setFrame(True)
        self.lineEdit_11.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMaximumSize(QSize(16777215, 25))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_15.setPalette(palette11)
        self.label_15.setFont(font3)
        self.label_15.setWordWrap(False)
        self.label_15.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_12 = QLineEdit(self.frame_6)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)
        self.lineEdit_12.setMinimumSize(QSize(200, 0))
        self.lineEdit_12.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_12.setSizeIncrement(QSize(0, 0))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_12.setPalette(palette12)
        self.lineEdit_12.setFont(font4)
        self.lineEdit_12.setFrame(True)
        self.lineEdit_12.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.lineEdit_12)


        self.horizontalLayout_6.addLayout(self.formLayout_2)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_10 = QSpacerItem(37, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_13)


        self.horizontalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.page_hpc_main)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush5 = QBrush(QColor(53, 53, 53, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.frame_8.setPalette(palette13)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(150, 16777215))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette14.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_5.setPalette(palette14)

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(150, 16777215))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette15.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_6.setPalette(palette15)

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.pushButton_9 = QPushButton(self.frame_8)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(150, 16777215))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette16.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_9.setPalette(palette16)

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(150, 16777215))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette17.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_7.setPalette(palette17)

        self.horizontalLayout_7.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(150, 16777215))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette18.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_8.setPalette(palette18)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)

        self.horizontalLayout_7.addWidget(self.pushButton_8)


        self.verticalLayout_17.addWidget(self.frame_8)


        self.verticalLayout_15.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)

        self.stackedWidget.addWidget(self.page_hpc_main)
        self.page_spc_main = QWidget()
        self.page_spc_main.setObjectName(u"page_spc_main")
        self.verticalLayout_12 = QVBoxLayout(self.page_spc_main)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.page_spc_main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_5.setPalette(palette19)
        self.label_5.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_5)

        self.frame_5 = QFrame(self.page_spc_main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(16777215, 25))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.label_2.setPalette(palette20)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"selection-color: rgb(255, 255, 255);")
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMinimumSize(QSize(350, 0))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_5.setSizeIncrement(QSize(0, 0))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
        palette21.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_5.setPalette(palette21)
        self.lineEdit_5.setFont(font4)
        self.lineEdit_5.setStyleSheet(u"text-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setBaseSize(QSize(0, 0))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label.setPalette(palette22)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMinimumSize(QSize(200, 0))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_3.setSizeIncrement(QSize(0, 0))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_3.setPalette(palette23)
        self.lineEdit_3.setFont(font4)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(16777215, 25))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_4.setPalette(palette24)
        self.label_4.setFont(font3)
        self.label_4.setWordWrap(False)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit.setPalette(palette25)
        self.lineEdit.setFont(font4)
        self.lineEdit.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.lineEdit.setFrame(True)
        self.lineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMaximumSize(QSize(16777215, 25))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_6.setPalette(palette26)
        self.label_6.setFont(font3)
        self.label_6.setWordWrap(False)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy3.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy3)
        self.lineEdit_4.setMinimumSize(QSize(200, 0))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 16777215))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_4.setPalette(palette27)
        self.lineEdit_4.setFont(font4)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setClearButtonEnabled(False)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMaximumSize(QSize(16777215, 25))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_3.setPalette(palette28)
        self.label_3.setFont(font3)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)
        self.lineEdit_2.setMinimumSize(QSize(200, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setSizeIncrement(QSize(0, 0))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
        palette29.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_2.setPalette(palette29)
        self.lineEdit_2.setFont(font4)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(16777215, 25))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_7.setPalette(palette30)
        self.label_7.setFont(font3)
        self.label_7.setWordWrap(False)
        self.label_7.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy3.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy3)
        self.lineEdit_6.setMinimumSize(QSize(200, 0))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_6.setSizeIncrement(QSize(0, 0))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush)
        palette31.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_6.setPalette(palette31)
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setClearButtonEnabled(False)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_6)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(37, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame = QFrame(self.page_spc_main)
        self.frame.setObjectName(u"frame")
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette32.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette32.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette32.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.frame_2.setPalette(palette32)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(150, 16777215))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette33.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_2.setPalette(palette33)

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 16777215))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette34.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton.setPalette(palette34)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(150, 16777215))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette35.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_3.setPalette(palette35)

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(150, 16777215))
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette36.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_4.setPalette(palette36)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_11.addWidget(self.frame, 0, Qt.AlignBottom)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.stackedWidget.addWidget(self.page_spc_main)
        self.page_hpc_material = QWidget()
        self.page_hpc_material.setObjectName(u"page_hpc_material")
        self.verticalLayout_22 = QVBoxLayout(self.page_hpc_material)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.page_hpc_material)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 50))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.Button, brush)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_16.setPalette(palette37)
        self.label_16.setFont(font2)

        self.verticalLayout_19.addWidget(self.label_16)

        self.checkBox = QCheckBox(self.page_hpc_material)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_19.addWidget(self.checkBox)

        self.frame_13 = QFrame(self.page_hpc_material)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMaximumSize(QSize(16777215, 25))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.Button, brush)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_20.setPalette(palette38)
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.label_20.setFont(font5)
        self.label_20.setWordWrap(False)
        self.label_20.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.spinBox = QSpinBox(self.frame_13)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 0))
        self.spinBox.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.spinBox)

        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMaximumSize(QSize(16777215, 25))
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.Button, brush)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_24.setPalette(palette39)
        self.label_24.setFont(font5)
        self.label_24.setWordWrap(False)
        self.label_24.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.horizontalLayout_10.addWidget(self.label_24)

        self.spinBox_2 = QSpinBox(self.frame_13)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.spinBox_2)


        self.verticalLayout_19.addWidget(self.frame_13, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.page_hpc_material)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.lineEdit_13 = QLineEdit(self.frame_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy3.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy3)
        self.lineEdit_13.setMinimumSize(QSize(0, 0))
        self.lineEdit_13.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_13.setSizeIncrement(QSize(0, 0))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush)
        palette40.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_13.setPalette(palette40)
        font6 = QFont()
        font6.setFamily(u"Helvetica")
        font6.setPointSize(10)
        self.lineEdit_13.setFont(font6)
        self.lineEdit_13.setStyleSheet(u"text-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.lineEdit_13.setFrame(True)
        self.lineEdit_13.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.frame_9)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy3.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy3)
        self.lineEdit_14.setMinimumSize(QSize(200, 0))
        self.lineEdit_14.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_14.setSizeIncrement(QSize(0, 0))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush)
        palette41.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_14.setPalette(palette41)
        self.lineEdit_14.setFont(font6)
        self.lineEdit_14.setFrame(True)
        self.lineEdit_14.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.frame_9)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy3.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy3)
        self.lineEdit_15.setMinimumSize(QSize(200, 0))
        self.lineEdit_15.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_15.setSizeIncrement(QSize(0, 0))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush)
        palette42.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_15.setPalette(palette42)
        self.lineEdit_15.setFont(font6)
        self.lineEdit_15.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.lineEdit_15.setFrame(True)
        self.lineEdit_15.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_15)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(1, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(7, QFormLayout.FieldRole, self.verticalSpacer_5)

        self.lineEdit_17 = QLineEdit(self.frame_9)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy3.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy3)
        self.lineEdit_17.setMinimumSize(QSize(200, 0))
        self.lineEdit_17.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_17.setSizeIncrement(QSize(0, 0))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush)
        palette43.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_17.setPalette(palette43)
        self.lineEdit_17.setFont(font6)
        self.lineEdit_17.setFrame(True)
        self.lineEdit_17.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.frame_9)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        sizePolicy3.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy3)
        self.lineEdit_18.setMinimumSize(QSize(200, 0))
        self.lineEdit_18.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_18.setSizeIncrement(QSize(0, 0))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush)
        palette44.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_18.setPalette(palette44)
        self.lineEdit_18.setFont(font6)
        self.lineEdit_18.setFrame(True)
        self.lineEdit_18.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.lineEdit_18)

        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMaximumSize(QSize(16777215, 25))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_22.setPalette(palette45)
        self.label_22.setFont(font5)
        self.label_22.setWordWrap(False)
        self.label_22.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_22)

        self.verticalSpacer_6 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(11, QFormLayout.FieldRole, self.verticalSpacer_7)

        self.lineEdit_16 = QLineEdit(self.frame_9)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy3.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy3)
        self.lineEdit_16.setMinimumSize(QSize(200, 0))
        self.lineEdit_16.setMaximumSize(QSize(16777215, 25))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.Button, brush)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.lineEdit_16.setPalette(palette46)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lineEdit_16)


        self.horizontalLayout_8.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.lineEdit_19 = QLineEdit(self.frame_9)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy3.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy3)
        self.lineEdit_19.setMinimumSize(QSize(0, 0))
        self.lineEdit_19.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_19.setSizeIncrement(QSize(0, 0))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush)
        palette47.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_19.setPalette(palette47)
        self.lineEdit_19.setFont(font6)
        self.lineEdit_19.setStyleSheet(u"text-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.lineEdit_19.setFrame(True)
        self.lineEdit_19.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.frame_9)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy3.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy3)
        self.lineEdit_20.setMinimumSize(QSize(200, 0))
        self.lineEdit_20.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_20.setSizeIncrement(QSize(0, 0))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush)
        palette48.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_20.setPalette(palette48)
        self.lineEdit_20.setFont(font6)
        self.lineEdit_20.setFrame(True)
        self.lineEdit_20.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_20)

        self.lineEdit_21 = QLineEdit(self.frame_9)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        sizePolicy3.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy3)
        self.lineEdit_21.setMinimumSize(QSize(200, 0))
        self.lineEdit_21.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_21.setSizeIncrement(QSize(0, 0))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush)
        palette49.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_21.setPalette(palette49)
        self.lineEdit_21.setFont(font6)
        self.lineEdit_21.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.lineEdit_21.setFrame(True)
        self.lineEdit_21.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lineEdit_21)

        self.verticalSpacer_8 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(1, QFormLayout.FieldRole, self.verticalSpacer_8)

        self.verticalSpacer_9 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_9)

        self.verticalSpacer_10 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_10)

        self.verticalSpacer_11 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(7, QFormLayout.FieldRole, self.verticalSpacer_11)

        self.lineEdit_22 = QLineEdit(self.frame_9)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        sizePolicy3.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
        self.lineEdit_22.setSizePolicy(sizePolicy3)
        self.lineEdit_22.setMinimumSize(QSize(200, 0))
        self.lineEdit_22.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_22.setSizeIncrement(QSize(0, 0))
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush)
        palette50.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_22.setPalette(palette50)
        self.lineEdit_22.setFont(font6)
        self.lineEdit_22.setFrame(True)
        self.lineEdit_22.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.lineEdit_22)

        self.lineEdit_23 = QLineEdit(self.frame_9)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        sizePolicy3.setHeightForWidth(self.lineEdit_23.sizePolicy().hasHeightForWidth())
        self.lineEdit_23.setSizePolicy(sizePolicy3)
        self.lineEdit_23.setMinimumSize(QSize(200, 0))
        self.lineEdit_23.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_23.setSizeIncrement(QSize(0, 0))
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush)
        palette51.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_23.setPalette(palette51)
        self.lineEdit_23.setFont(font6)
        self.lineEdit_23.setFrame(True)
        self.lineEdit_23.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.lineEdit_23)

        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMaximumSize(QSize(16777215, 25))
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_23.setPalette(palette52)
        self.label_23.setFont(font5)
        self.label_23.setWordWrap(False)
        self.label_23.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.label_23)

        self.verticalSpacer_12 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_12)

        self.verticalSpacer_13 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(11, QFormLayout.FieldRole, self.verticalSpacer_13)

        self.lineEdit_24 = QLineEdit(self.frame_9)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        sizePolicy3.setHeightForWidth(self.lineEdit_24.sizePolicy().hasHeightForWidth())
        self.lineEdit_24.setSizePolicy(sizePolicy3)
        self.lineEdit_24.setMinimumSize(QSize(200, 0))
        self.lineEdit_24.setMaximumSize(QSize(16777215, 25))
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.Button, brush)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.lineEdit_24.setPalette(palette53)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.lineEdit_24)


        self.horizontalLayout_8.addLayout(self.formLayout_4)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy6)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_19.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.page_hpc_material)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy5.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy5)
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette54.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.frame_12.setPalette(palette54)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(150, 16777215))
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette55.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_10.setPalette(palette55)

        self.horizontalLayout_9.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(150, 16777215))
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette56.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette56.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_11.setPalette(palette56)

        self.horizontalLayout_9.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_12)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(150, 16777215))
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette57.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette57.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_12.setPalette(palette57)

        self.horizontalLayout_9.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_12)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(150, 16777215))
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette58.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette58.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette58.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pushButton_13.setPalette(palette58)
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setFlat(False)

        self.horizontalLayout_9.addWidget(self.pushButton_13)


        self.verticalLayout_21.addWidget(self.frame_12)


        self.verticalLayout_19.addWidget(self.frame_11, 0, Qt.AlignBottom)


        self.verticalLayout_22.addLayout(self.verticalLayout_19)

        self.stackedWidget.addWidget(self.page_hpc_material)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.stackedWidget.addWidget(self.page_16)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText("")
        self.Btn_hpc.setText(QCoreApplication.translate("MainWindow", u" HPC - Hard Plastic Component", None))
        self.Btn_hpc_main.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_hpc_process.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_hpc_mat.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_hpc_qc.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_hpc_manu.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_hpc_pack.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_spc.setText(QCoreApplication.translate("MainWindow", u"SPC - Soft Plastic Component", None))
        self.Btn_spc_main.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_spc_process.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_spc_mat.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_spc_qc.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_spc_manu.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_spc_pack.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_dpc.setText(QCoreApplication.translate("MainWindow", u"DPC - Dual Plastic Component", None))
        self.Btn_dpc_main.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_dpc_process.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_dpc_mat.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_dpc_qc.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_dpc_manu.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_dpc_pack.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_ssc.setText(QCoreApplication.translate("MainWindow", u"SSC - Stainless Steel Component", None))
        self.Btn_ssc_main.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_ssc_process.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_ssc_mat.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_ssc_qc.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_ssc_manu.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_ssc_pack.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_alc.setText(QCoreApplication.translate("MainWindow", u"ALC - Aluminum Component", None))
        self.Btn_alc_main.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_alc_process.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_alc_mat.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_alc_qc.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_alc_manu.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_alc_pack.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_cmt.setText(QCoreApplication.translate("MainWindow", u"CMT - Cut Make Trim", None))
        self.Btn_cmt_main.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_cmt_process.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_cmt_mat.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_cmt_qc.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_cmt_manu.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_cmt_pack.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> HPC -  Main Page</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Component/Part Name</span></p></body></html>", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Inventory Level Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">EST Component/Part Number</span></p></body></html>", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HPC000-NAT00", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Supplier Name</span></p></body></html>", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Supplier Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Number of Colours</span></p></body></html>", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. 3", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Author Name</span></p></body></html>", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. John Smith", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Revision Number</span></p></body></html>", None))
        self.lineEdit_12.setInputMask("")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for No Changes", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> SPC -  Main Page</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Component/Part Name</span></p></body></html>", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Inventory Level Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">EST Component/Part Number</span></p></body></html>", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HPC000-NAT00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Supplier Name</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Supplier Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Number of Colours</span></p></body></html>", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. 3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Author Name</span></p></body></html>", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. John Smith", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Revision Number</span></p></body></html>", None))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for No Changes", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\"> HPC -  MATERIAL</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Number of Colours</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Number of Materials</span></p></body></html>", None))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Inventory Level Name", None))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HPC000-NAT00", None))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Supplier Name", None))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. John Smith", None))
        self.lineEdit_18.setInputMask("")
        self.lineEdit_18.setText("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for No Changes", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Revision Number</span></p></body></html>", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Inventory Level Name", None))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HPC000-NAT00", None))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Supplier Name", None))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. John Smith", None))
        self.lineEdit_23.setInputMask("")
        self.lineEdit_23.setText("")
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for No Changes", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Revision Number</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

