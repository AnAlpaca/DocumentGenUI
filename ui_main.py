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
        MainWindow.resize(1238, 718)
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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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
        self.Btn_hpc_main_2 = QPushButton(self.frame_spc)
        self.Btn_hpc_main_2.setObjectName(u"Btn_hpc_main_2")
        self.Btn_hpc_main_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_main_2.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_main_2.setSizePolicy(sizePolicy1)
        self.Btn_hpc_main_2.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_main_2.setFont(font1)
        self.Btn_hpc_main_2.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_main_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_hpc_main_2)

        self.Btn_hpc_process_2 = QPushButton(self.frame_spc)
        self.Btn_hpc_process_2.setObjectName(u"Btn_hpc_process_2")
        self.Btn_hpc_process_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_process_2.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_process_2.setSizePolicy(sizePolicy1)
        self.Btn_hpc_process_2.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_process_2.setFont(font1)
        self.Btn_hpc_process_2.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_process_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_hpc_process_2)

        self.Btn_hpc_mat_2 = QPushButton(self.frame_spc)
        self.Btn_hpc_mat_2.setObjectName(u"Btn_hpc_mat_2")
        self.Btn_hpc_mat_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_mat_2.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_mat_2.setSizePolicy(sizePolicy1)
        self.Btn_hpc_mat_2.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_mat_2.setFont(font1)
        self.Btn_hpc_mat_2.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_mat_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_hpc_mat_2)

        self.Btn_hpc_qc_2 = QPushButton(self.frame_spc)
        self.Btn_hpc_qc_2.setObjectName(u"Btn_hpc_qc_2")
        self.Btn_hpc_qc_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_qc_2.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_qc_2.setSizePolicy(sizePolicy1)
        self.Btn_hpc_qc_2.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_qc_2.setFont(font1)
        self.Btn_hpc_qc_2.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_qc_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_hpc_qc_2)

        self.Btn_hpc_manu_2 = QPushButton(self.frame_spc)
        self.Btn_hpc_manu_2.setObjectName(u"Btn_hpc_manu_2")
        self.Btn_hpc_manu_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_manu_2.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_manu_2.setSizePolicy(sizePolicy1)
        self.Btn_hpc_manu_2.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_manu_2.setFont(font1)
        self.Btn_hpc_manu_2.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_manu_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_hpc_manu_2)

        self.Btn_hpc_pack_2 = QPushButton(self.frame_spc)
        self.Btn_hpc_pack_2.setObjectName(u"Btn_hpc_pack_2")
        self.Btn_hpc_pack_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_pack_2.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_pack_2.setSizePolicy(sizePolicy1)
        self.Btn_hpc_pack_2.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_pack_2.setFont(font1)
        self.Btn_hpc_pack_2.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_pack_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_hpc_pack_2)


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
        self.Btn_hpc_main_3 = QPushButton(self.frame_dpc)
        self.Btn_hpc_main_3.setObjectName(u"Btn_hpc_main_3")
        self.Btn_hpc_main_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_main_3.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_main_3.setSizePolicy(sizePolicy1)
        self.Btn_hpc_main_3.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_main_3.setFont(font1)
        self.Btn_hpc_main_3.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_main_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_hpc_main_3)

        self.Btn_hpc_process_3 = QPushButton(self.frame_dpc)
        self.Btn_hpc_process_3.setObjectName(u"Btn_hpc_process_3")
        self.Btn_hpc_process_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_process_3.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_process_3.setSizePolicy(sizePolicy1)
        self.Btn_hpc_process_3.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_process_3.setFont(font1)
        self.Btn_hpc_process_3.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_process_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_hpc_process_3)

        self.Btn_hpc_mat_3 = QPushButton(self.frame_dpc)
        self.Btn_hpc_mat_3.setObjectName(u"Btn_hpc_mat_3")
        self.Btn_hpc_mat_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_mat_3.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_mat_3.setSizePolicy(sizePolicy1)
        self.Btn_hpc_mat_3.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_mat_3.setFont(font1)
        self.Btn_hpc_mat_3.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_mat_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_hpc_mat_3)

        self.Btn_hpc_qc_3 = QPushButton(self.frame_dpc)
        self.Btn_hpc_qc_3.setObjectName(u"Btn_hpc_qc_3")
        self.Btn_hpc_qc_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_qc_3.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_qc_3.setSizePolicy(sizePolicy1)
        self.Btn_hpc_qc_3.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_qc_3.setFont(font1)
        self.Btn_hpc_qc_3.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_qc_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_hpc_qc_3)

        self.Btn_hpc_manu_3 = QPushButton(self.frame_dpc)
        self.Btn_hpc_manu_3.setObjectName(u"Btn_hpc_manu_3")
        self.Btn_hpc_manu_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_manu_3.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_manu_3.setSizePolicy(sizePolicy1)
        self.Btn_hpc_manu_3.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_manu_3.setFont(font1)
        self.Btn_hpc_manu_3.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_manu_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_hpc_manu_3)

        self.Btn_hpc_pack_3 = QPushButton(self.frame_dpc)
        self.Btn_hpc_pack_3.setObjectName(u"Btn_hpc_pack_3")
        self.Btn_hpc_pack_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_pack_3.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_pack_3.setSizePolicy(sizePolicy1)
        self.Btn_hpc_pack_3.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_pack_3.setFont(font1)
        self.Btn_hpc_pack_3.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_pack_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_hpc_pack_3)


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
        self.Btn_hpc_main_6 = QPushButton(self.frame_ssc)
        self.Btn_hpc_main_6.setObjectName(u"Btn_hpc_main_6")
        self.Btn_hpc_main_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_main_6.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_main_6.setSizePolicy(sizePolicy1)
        self.Btn_hpc_main_6.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_main_6.setFont(font1)
        self.Btn_hpc_main_6.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_main_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_hpc_main_6)

        self.Btn_hpc_process_6 = QPushButton(self.frame_ssc)
        self.Btn_hpc_process_6.setObjectName(u"Btn_hpc_process_6")
        self.Btn_hpc_process_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_process_6.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_process_6.setSizePolicy(sizePolicy1)
        self.Btn_hpc_process_6.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_process_6.setFont(font1)
        self.Btn_hpc_process_6.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_process_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_hpc_process_6)

        self.Btn_hpc_mat_6 = QPushButton(self.frame_ssc)
        self.Btn_hpc_mat_6.setObjectName(u"Btn_hpc_mat_6")
        self.Btn_hpc_mat_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_mat_6.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_mat_6.setSizePolicy(sizePolicy1)
        self.Btn_hpc_mat_6.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_mat_6.setFont(font1)
        self.Btn_hpc_mat_6.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_mat_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_hpc_mat_6)

        self.Btn_hpc_qc_6 = QPushButton(self.frame_ssc)
        self.Btn_hpc_qc_6.setObjectName(u"Btn_hpc_qc_6")
        self.Btn_hpc_qc_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_qc_6.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_qc_6.setSizePolicy(sizePolicy1)
        self.Btn_hpc_qc_6.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_qc_6.setFont(font1)
        self.Btn_hpc_qc_6.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_qc_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_hpc_qc_6)

        self.Btn_hpc_manu_6 = QPushButton(self.frame_ssc)
        self.Btn_hpc_manu_6.setObjectName(u"Btn_hpc_manu_6")
        self.Btn_hpc_manu_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_manu_6.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_manu_6.setSizePolicy(sizePolicy1)
        self.Btn_hpc_manu_6.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_manu_6.setFont(font1)
        self.Btn_hpc_manu_6.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_manu_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_hpc_manu_6)

        self.Btn_hpc_pack_6 = QPushButton(self.frame_ssc)
        self.Btn_hpc_pack_6.setObjectName(u"Btn_hpc_pack_6")
        self.Btn_hpc_pack_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_pack_6.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_pack_6.setSizePolicy(sizePolicy1)
        self.Btn_hpc_pack_6.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_pack_6.setFont(font1)
        self.Btn_hpc_pack_6.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_pack_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.Btn_hpc_pack_6)


        self.verticalLayout_2.addWidget(self.frame_ssc)

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
        self.Btn_hpc_main_4 = QPushButton(self.frame_alc)
        self.Btn_hpc_main_4.setObjectName(u"Btn_hpc_main_4")
        self.Btn_hpc_main_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_main_4.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_main_4.setSizePolicy(sizePolicy1)
        self.Btn_hpc_main_4.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_main_4.setFont(font1)
        self.Btn_hpc_main_4.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_main_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_hpc_main_4)

        self.Btn_hpc_process_4 = QPushButton(self.frame_alc)
        self.Btn_hpc_process_4.setObjectName(u"Btn_hpc_process_4")
        self.Btn_hpc_process_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_process_4.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_process_4.setSizePolicy(sizePolicy1)
        self.Btn_hpc_process_4.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_process_4.setFont(font1)
        self.Btn_hpc_process_4.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_process_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_hpc_process_4)

        self.Btn_hpc_mat_4 = QPushButton(self.frame_alc)
        self.Btn_hpc_mat_4.setObjectName(u"Btn_hpc_mat_4")
        self.Btn_hpc_mat_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_mat_4.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_mat_4.setSizePolicy(sizePolicy1)
        self.Btn_hpc_mat_4.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_mat_4.setFont(font1)
        self.Btn_hpc_mat_4.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_mat_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_hpc_mat_4)

        self.Btn_hpc_qc_4 = QPushButton(self.frame_alc)
        self.Btn_hpc_qc_4.setObjectName(u"Btn_hpc_qc_4")
        self.Btn_hpc_qc_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_qc_4.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_qc_4.setSizePolicy(sizePolicy1)
        self.Btn_hpc_qc_4.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_qc_4.setFont(font1)
        self.Btn_hpc_qc_4.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_qc_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_hpc_qc_4)

        self.Btn_hpc_manu_4 = QPushButton(self.frame_alc)
        self.Btn_hpc_manu_4.setObjectName(u"Btn_hpc_manu_4")
        self.Btn_hpc_manu_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_manu_4.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_manu_4.setSizePolicy(sizePolicy1)
        self.Btn_hpc_manu_4.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_manu_4.setFont(font1)
        self.Btn_hpc_manu_4.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_manu_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_hpc_manu_4)

        self.Btn_hpc_pack_4 = QPushButton(self.frame_alc)
        self.Btn_hpc_pack_4.setObjectName(u"Btn_hpc_pack_4")
        self.Btn_hpc_pack_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_pack_4.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_pack_4.setSizePolicy(sizePolicy1)
        self.Btn_hpc_pack_4.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_pack_4.setFont(font1)
        self.Btn_hpc_pack_4.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_pack_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_hpc_pack_4)


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
        self.Btn_hpc_main_5 = QPushButton(self.frame_cmt)
        self.Btn_hpc_main_5.setObjectName(u"Btn_hpc_main_5")
        self.Btn_hpc_main_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_main_5.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_main_5.setSizePolicy(sizePolicy1)
        self.Btn_hpc_main_5.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_main_5.setFont(font1)
        self.Btn_hpc_main_5.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_main_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_hpc_main_5)

        self.Btn_hpc_process_5 = QPushButton(self.frame_cmt)
        self.Btn_hpc_process_5.setObjectName(u"Btn_hpc_process_5")
        self.Btn_hpc_process_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_process_5.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_process_5.setSizePolicy(sizePolicy1)
        self.Btn_hpc_process_5.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_process_5.setFont(font1)
        self.Btn_hpc_process_5.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_process_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_hpc_process_5)

        self.Btn_hpc_mat_5 = QPushButton(self.frame_cmt)
        self.Btn_hpc_mat_5.setObjectName(u"Btn_hpc_mat_5")
        self.Btn_hpc_mat_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_mat_5.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_mat_5.setSizePolicy(sizePolicy1)
        self.Btn_hpc_mat_5.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_mat_5.setFont(font1)
        self.Btn_hpc_mat_5.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_mat_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_hpc_mat_5)

        self.Btn_hpc_qc_5 = QPushButton(self.frame_cmt)
        self.Btn_hpc_qc_5.setObjectName(u"Btn_hpc_qc_5")
        self.Btn_hpc_qc_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_qc_5.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_qc_5.setSizePolicy(sizePolicy1)
        self.Btn_hpc_qc_5.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_qc_5.setFont(font1)
        self.Btn_hpc_qc_5.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_qc_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_hpc_qc_5)

        self.Btn_hpc_manu_5 = QPushButton(self.frame_cmt)
        self.Btn_hpc_manu_5.setObjectName(u"Btn_hpc_manu_5")
        self.Btn_hpc_manu_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_manu_5.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_manu_5.setSizePolicy(sizePolicy1)
        self.Btn_hpc_manu_5.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_manu_5.setFont(font1)
        self.Btn_hpc_manu_5.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_manu_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_hpc_manu_5)

        self.Btn_hpc_pack_5 = QPushButton(self.frame_cmt)
        self.Btn_hpc_pack_5.setObjectName(u"Btn_hpc_pack_5")
        self.Btn_hpc_pack_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Btn_hpc_pack_5.sizePolicy().hasHeightForWidth())
        self.Btn_hpc_pack_5.setSizePolicy(sizePolicy1)
        self.Btn_hpc_pack_5.setMinimumSize(QSize(0, 0))
        self.Btn_hpc_pack_5.setFont(font1)
        self.Btn_hpc_pack_5.setLayoutDirection(Qt.LeftToRight)
        self.Btn_hpc_pack_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.Btn_hpc_pack_5)


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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
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
        self.label_5.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(24)
        self.label_5.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_5)

        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setBaseSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label.setPalette(palette1)
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMinimumSize(QSize(200, 0))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_3.setSizeIncrement(QSize(0, 0))
        palette2 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
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
        self.lineEdit_3.setPalette(palette2)
        font4 = QFont()
        font4.setFamily(u"Helvetica")
        font4.setPointSize(14)
        self.lineEdit_3.setFont(font4)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(16777215, 25))
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
        self.label_4.setPalette(palette3)
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
        self.lineEdit.setPalette(palette4)
        self.lineEdit.setFont(font4)
        self.lineEdit.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.lineEdit.setFrame(True)
        self.lineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(16777215, 25))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.label_2.setPalette(palette5)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"selection-color: rgb(255, 255, 255);")
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy3.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy3)
        self.lineEdit_4.setMinimumSize(QSize(200, 0))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 16777215))
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
        self.lineEdit_4.setPalette(palette6)
        self.lineEdit_4.setFont(font4)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setClearButtonEnabled(False)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)
        self.lineEdit_2.setMinimumSize(QSize(200, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setSizeIncrement(QSize(0, 0))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_2.setPalette(palette7)
        self.lineEdit_2.setFont(font4)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_6 = QLineEdit(self.frame_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy3.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy3)
        self.lineEdit_6.setMinimumSize(QSize(200, 0))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_6.setSizeIncrement(QSize(0, 0))
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
        self.lineEdit_6.setPalette(palette8)
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setClearButtonEnabled(False)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMaximumSize(QSize(16777215, 25))
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
        self.label_3.setPalette(palette9)
        self.label_3.setFont(font3)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_3)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMaximumSize(QSize(16777215, 25))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.label_6.setPalette(palette10)
        self.label_6.setFont(font3)
        self.label_6.setWordWrap(False)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(16777215, 25))
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
        self.label_7.setPalette(palette11)
        self.label_7.setFont(font3)
        self.label_7.setWordWrap(False)
        self.label_7.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMinimumSize(QSize(350, 0))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_5.setSizeIncrement(QSize(0, 0))
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
        self.lineEdit_5.setPalette(palette12)
        self.lineEdit_5.setFont(font4)
        self.lineEdit_5.setStyleSheet(u"text-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
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

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


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
        self.Btn_hpc_main_2.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_hpc_process_2.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_hpc_mat_2.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_hpc_qc_2.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_hpc_manu_2.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_hpc_pack_2.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_dpc.setText(QCoreApplication.translate("MainWindow", u"DPC - Dual Plastic Component", None))
        self.Btn_hpc_main_3.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_hpc_process_3.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_hpc_mat_3.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_hpc_qc_3.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_hpc_manu_3.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_hpc_pack_3.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_ssc.setText(QCoreApplication.translate("MainWindow", u"SSC - Stainless Steel Component", None))
        self.Btn_hpc_main_6.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_hpc_process_6.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_hpc_mat_6.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_hpc_qc_6.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_hpc_manu_6.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_hpc_pack_6.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_alc.setText(QCoreApplication.translate("MainWindow", u"ALC - Aluminum Component", None))
        self.Btn_hpc_main_4.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_hpc_process_4.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_hpc_mat_4.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_hpc_qc_4.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_hpc_manu_4.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_hpc_pack_4.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.Btn_cmt.setText(QCoreApplication.translate("MainWindow", u"CMT - Cut Make Trim", None))
        self.Btn_hpc_main_5.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.Btn_hpc_process_5.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Btn_hpc_mat_5.setText(QCoreApplication.translate("MainWindow", u"Materials and Masterbatch", None))
        self.Btn_hpc_qc_5.setText(QCoreApplication.translate("MainWindow", u"Quality Concerns", None))
        self.Btn_hpc_manu_5.setText(QCoreApplication.translate("MainWindow", u"Manufacturing Requirements", None))
        self.Btn_hpc_pack_5.setText(QCoreApplication.translate("MainWindow", u"Packaging", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> Main Page</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">EST Component/Part Number</span></p></body></html>", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HPC000-NAT00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Supplier Name</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Supplier Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Component/Part Name</span></p></body></html>", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. 3", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Eg. John Smith", None))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for No Changes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Author Name</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Number of Colours</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Revision Number</span></p></body></html>", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Inventory Level Name", None))
    # retranslateUi

