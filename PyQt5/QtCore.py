'''
Created on 5 Apr 2023

@author: Rob Probin
'''
import os
import inspect

class Qt():
    '''
    Qt
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {params}")

    class PenStyle(): 
        NoPen = None

    ScrollBarAlwaysOn = 5
    SolidPattern = 10
    Horizontal = 20
    AutoText = 30
    yellow = 0xFFFF00
    
# fake version        
QT_VERSION_STR = "1.0.0"

class QDir():
    @staticmethod
    def currentPath():
        return os.getcwd()
        #return os.path.dirname(os.path.realpath(__file__))    # current Python file path

class QByteArray():
    def __init__(self):
        self.array_size = 0
    
    def size(self):
        return self.array_size

QFile = None
QFileInfo = None
QSaveFile = None

class QSettings():
    def __init__(self, group, setting):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {group} {setting}")

    def value(self, setting, destination):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {setting} {destination}")
        return destination

QTextStream = None

class pyqtSignal():
    def __init__(self, x, y, z):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x} {y} {z}")
    
QPoint = None
QPointF = None


class QSize():
    def __init__(self, x, y):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x} {y}")
   
class QRect():
    def __init__(self, x1, y1, x2, y2):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x1} {y1} {x2} {y2}")
    
    
class QCoreApplication():
    @staticmethod
    def translate(window, text):
        print(f"QCoreApplication::translate {window} {text}")
    
class QMetaObject():
    @staticmethod
    def connectSlotsByName(window):
        print(f"QMetaObject::connectSlotsByName {window}")
    
    