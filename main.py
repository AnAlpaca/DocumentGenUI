################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## TOGGLE SUB MENUS
        ########################################################################
        #self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))
        self.ui.Btn_hpc.clicked.connect(lambda: UIFunctions.openSubMenu(self, 240, self.ui.frame_hpc, True))
        self.ui.Btn_spc.clicked.connect(lambda: UIFunctions.openSubMenu(self, 240, self.ui.frame_spc, True))
        self.ui.Btn_dpc.clicked.connect(lambda: UIFunctions.openSubMenu(self, 240, self.ui.frame_dpc, True))
        self.ui.Btn_ssc.clicked.connect(lambda: UIFunctions.openSubMenu(self, 240, self.ui.frame_ssc, True))
        self.ui.Btn_alc.clicked.connect(lambda: UIFunctions.openSubMenu(self, 240, self.ui.frame_alc, True))
        self.ui.Btn_cmt.clicked.connect(lambda: UIFunctions.openSubMenu(self, 240, self.ui.frame_cmt, True))
        
        
        ## NAVIGATING PAGES
        self.ui.Btn_spc_main.clicked.connect(lambda: UIFunctions.handleButton(self, 1))
        self.ui.Btn_hpc_main.clicked.connect(lambda: UIFunctions.handleButton(self, 0))
        self.ui.Btn_hpc_mat.clicked.connect(lambda: UIFunctions.handleButton(self, 2))
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


