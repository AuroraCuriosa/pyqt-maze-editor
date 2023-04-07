'''
Created on 5 Apr 2023

@author: Rob Probin
'''
import os

class Qt():
    '''
    Qt
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
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
        pass

    def value(self, setting, destination):
        return destination

QTextStream = None

class pyqtSignal():
    def __init__(self, x, y, z):
        pass
    
QPoint = None
QPointF = None


class QSize():
    def __init__(self, x, y):
        pass
    
class QRect():
    def __init__(self, x1, y1, x2, y2):
        pass
    
    
class QCoreApplication():
    @staticmethod
    def translate(window, text):
        pass
    
class QMetaObject():
    @staticmethod
    def connectSlotsByName(window):
        pass
    
    