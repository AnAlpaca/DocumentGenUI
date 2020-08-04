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


        
    def closeSubMenu(self, ui_element, enable):
        operator = ui_element
        if enable:

        #Get height
            height = operator.height()
            standard = 0

        #Set max Width, this controls the size of the expansion of the left frame when clicked
            if height != 0:
                heightClose = standard
                self.animation_subframe_min = QPropertyAnimation(operator, b"minimumHeight") 
                self.animation_subframe_min.setDuration(5)
                self.animation_subframe_min.setStartValue(height)
                self.animation_subframe_min.setEndValue(heightClose)
                self.animation_subframe_min.start()
                self.animation_subframe_max = QPropertyAnimation(operator, b"maximumHeight") 
                self.animation_subframe_max.setDuration(5)
                self.animation_subframe_max.setStartValue(height)
                self.animation_subframe_max.setEndValue(heightClose)
                self.animation_subframe_max.start()            
            else:
                pass
        
    def closeAllSubMenus(self, exception, enable):
        if enable:
            operator = exception
            catergories = [self.ui.frame_hpc, self.ui.frame_spc, self.ui.frame_dpc, self.ui.frame_ssc, self.ui.frame_alc, self.ui.frame_cmt]
            for i in range(len(catergories)):
                if operator != catergories[i]:
                    UIFunctions.closeSubMenu(self, catergories[i], True)
                else:
                    pass
# interetsing behaviour here where is closes, youll see when you try it.
    def openSubMenu(self, maxHeight, ui_element, enable):
        
        operator = ui_element
        if enable:

            #Get height
            height = operator.height()
            maxExtend = maxHeight
            standard = 0

            #Set max height, this controls the size of the sub frames when clicked
            if height == 0:
                heightExpand = maxExtend
            
            else:
                heightExpand = standard

            # Setting up Animation of the frame expanding and contracting
            self.animation_subframe_min = QPropertyAnimation(operator, b"minimumHeight") 
            self.animation_subframe_min.setDuration(200)
            self.animation_subframe_min.setStartValue(height)
            self.animation_subframe_min.setEndValue(heightExpand)
            self.animation_subframe_min.start()
            self.animation_subframe_max = QPropertyAnimation(operator, b"maximumHeight") 
            self.animation_subframe_max.setDuration(200)
            self.animation_subframe_max.setStartValue(height)
            self.animation_subframe_max.setEndValue(heightExpand)
            self.animation_subframe_max.start()
            UIFunctions.closeAllSubMenus(self, ui_element, True)