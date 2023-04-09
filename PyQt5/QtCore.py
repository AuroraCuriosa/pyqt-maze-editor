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

class QFile():
    def __init__(self, filename):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename}")
        self._filename = filename
    


class QFileInfo():
    def __init__(self, filename):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename}")
        self._filename = filename
    
    def fileName(self):
        return self._filename

    
class QSaveFile():
    def __init__(self, filename):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {filename}")
        self._filename = filename


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
    def __init__(self, arg1=None, arg2=None, arg3=None):
        if arg1 is not None:
            if arg2 is not None:
                if arg3 is not None:
                    self._notify_observers = self._notify_observers3
                else:
                    self._notify_observers = self._notify_observers2
            else:
                self._notify_observers = self._notify_observers1
        else:
            self._notify_observers = self._notify_observers0

        self._observers = []
        
    def connect(self, function):
        self._observers.append(function)
    
    def _notify_observers0(self):
        for observer in self._observers:
            observer()

    def _notify_observers1(self, param1):
        for observer in self._observers:
            observer(param1)

    def _notify_observers2(self, param1, param2):
        for observer in self._observers:
            observer(param1, param2)

    def _notify_observers3(self, param1, param2, param3):
        for observer in self._observers:
            observer(param1, param2, param3)
 
 
class QPoint():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def x(self):
        return self._x
    def y(self):
        return self._y

class QPointF():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def x(self):
        return self._x
    def y(self):
        return self._y


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
    
    