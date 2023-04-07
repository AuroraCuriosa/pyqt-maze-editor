'''
Created on 5 Apr 2023

@author: Rob Probin
'''

class QIcon():
    '''
    QtGui
    '''

    def __init__(self, filename=None):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def fromTheme(theme):
        pass
    
    def addPixmap(self, filename, param1, param2):
        pass
    
    Normal = 1
    On = True
    
class QPixmap():
    def __init__(self, filename):
        pass
    
    
class QKeySequence():
    @staticmethod
    def New():
        pass
    @staticmethod
    def Open():
        pass
    @staticmethod
    def Save():
        pass
    @staticmethod
    def SaveAs():
        pass
    @staticmethod
    def Quit():
        pass
    
    #@staticmethod
    #def setShortcut(param):
    #    pass
    
    

class QBrush():
    def __init__(self, param):
        pass
    
    def setStyle(self, param):
        pass
    
QPen = None

class QColor():
    def __init__(self, r, g=None, b=None):
        if g is not None:
            r = (r << 16) + (g << 8) + b

        self.colour = r

QPicture = None

class QFont():
    def __init__(self):
        pass
    def setBold(self, state):
        pass
    
    def setWeight(self, weight):
        pass
    
QPainter = None
QFontMetrics = None


