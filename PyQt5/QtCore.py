'''
Created on 5 Apr 2023

@author: Rob Probin
'''
from test.test_funcattrs import StaticMethodAttrsTest

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
    
# fake version        
QT_VERSION_STR = "1.0.0"

class QDir():
    @staticmethod
    def currentPath():
        pass
    

QByteArray = None
QFile = None
QFileInfo = None
QSaveFile = None
QSettings = None
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
    
    