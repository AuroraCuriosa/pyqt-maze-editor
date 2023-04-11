'''
Created on 5 Apr 2023

@author: Rob Probin
'''

import inspect
import pygame
from PyQt5.QtCore import QtBase


class QIcon(QtBase):
    '''
    QtGui
    '''

    def __init__(self, filename=None):
        '''
        Constructor
        '''
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename}")
        if filename is not None:
            self._image = pygame.image.load(filename)
            width, height = self._image.get_size()
            self.x, self.y = QtBase._Our_App_Instance.get_current_GUI_container().add_child(self, width, height)
        else:
            self._image = None
        
        
    @staticmethod
    def fromTheme(theme):
        print(f"QIcon::fromTheme {theme}")
    
    def addPixmap(self, pixmap, param1, param2):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} don't use parameters {param1} {param2}")
        self._image = pixmap.get_image()
        width, height = self._image.get_size()
        self.x, self.y = QtBase._Our_App_Instance.get_current_GUI_container().add_child(self, width, height)
        
        # override class items
        self.Normal = param1
        self.On = param2
        
    Normal = 1
    On = True
    
    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))
    
class QPixmap():
    def __init__(self, filename):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename}")
        self._image = pygame.image.load(filename)

    def get_image(self):
        return self._image
    
class QKeySequence():
    @staticmethod
    def New():
        print("QKeySequence::New")
        
    @staticmethod
    def Open():
        print("QKeySequence::Open")

    @staticmethod
    def Save():
        print("QKeySequence::Save")

    @staticmethod
    def SaveAs():
        print("QKeySequence::SaveAs")

    @staticmethod
    def Quit():
        print("QKeySequence::Quit")
        
    

class QBrush():
    def __init__(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def setStyle(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
QPen = None

class QColor():
    def __init__(self, r, g=None, b=None):
        if g is not None:
            r = (r << 16) + (g << 8) + b

        self.colour = r

QPicture = None

class QFont():
    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")

    def setBold(self, state):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {state}")
    
    def setWeight(self, weight):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {weight}")
    
QPainter = None
QFontMetrics = None


