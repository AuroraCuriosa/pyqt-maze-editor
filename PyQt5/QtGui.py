'''
Created on 5 Apr 2023

@author: Rob Probin
'''

import inspect

class QIcon():
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

    
    @staticmethod
    def fromTheme(theme):
        print(f"QIcon::fromTheme {theme}")
    
    def addPixmap(self, filename, param1, param2):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename} {param1} {param2}")
    
    Normal = 1
    On = True
    
class QPixmap():
    def __init__(self, filename):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename}")
    
    
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


