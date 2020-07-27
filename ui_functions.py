######################################
# BY AN_ALPACA                       #    
# ADAPTED FROM WANDERSON M. PIMENTA  #
######################################

from main import*

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            #Get Width
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            #Set max Width, this controls the size of the expansion of the left frame when clicked
            if width == 70:
                widthExtended = maxExtend
            
            else:
                widthExtended = standard

            # Setting up Animation of the frame expanding and contracting
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth") 
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()