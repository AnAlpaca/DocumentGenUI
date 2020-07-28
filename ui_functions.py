######################################
# BY AN_ALPACA                       #    
# ADAPTED FROM WANDERSON M. PIMENTA  #
######################################

from main import*

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            #Get Width
            width = self.ui.frame_left_extra.width()
            maxExtend = maxWidth
            standard = 10

            #Set max Width, this controls the size of the expansion of the left frame when clicked
            if width == 10:
                widthExtended = maxExtend
            
            else:
                widthExtended = standard

            # Setting up Animation of the frame expanding and contracting
            self.animation = QPropertyAnimation(self.ui.frame_left_extra, b"minimumWidth") 
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def openSubMenu(self, maxHeight, enable):
        if enable:

            #Get Width
            height = self.ui.Btn_Menu_3.height()
            maxExtend = maxHeight
            standard = 40

            #Set max Width, this controls the size of the expansion of the left frame when clicked
            if height == 40:
                heightExpand = maxExtend
            
            else:
                heightExpand = standard

            # Setting up Animation of the frame expanding and contracting
            self.animation = QPropertyAnimation(self.ui.Btn_Menu_3, b"minimumHeight") 
            self.animation.setDuration(400)
            self.animation.setStartValue(height)
            self.animation.setEndValue(heightExpand)
            self.animation.start()            