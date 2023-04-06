'''
Created on 5 Apr 2023

@author: Rob Probin
'''
from pip._vendor.pyparsing.helpers import opAssoc
from tkinter.dnd import Icon
from test.test_funcattrs import StaticMethodAttrsTest

class QApplication():
    '''
    Fake QApplication
    '''


    def __init__(self, args):
        '''
        Constructor
        '''
        pass
    
    
  
class QFrame():
    NoFrame = 1
    HLine = 2
    Sunken = 3
      
    def __init__(self, widget):
        pass
    
    def setFrameShape(self, type):
        pass
    
    def setFrameShadow(self, type):
        pass

    def setObjectName(self, name):
        pass

class QLabel():
    def __init__(self, widget):
        pass

    def setFont(self, font):
        pass
    
    def setObjectName(self, name):
        pass
    
    def setTextFormat(self, param):
        pass
    
    def setText(self, text):
        pass

    
class QMainWindow():
    def __init__(self):
        self.menu = None
    
    def setObjectName(self, name):
        pass
    
    def resize(self, x, y):
        print("resize")
    
    @staticmethod
    def setWindowIcon(icon):
        print("setWindowIcon")
        
    def setVerticalScrollBarPolicy(self, x):
        print("setVerticalScrollBarPolicy")

    def setHorizontalScrollBarPolicy(self, x):
        print("setHorizontalScrollBarPolicy")
    
    def setCentralWidget(self, widget):
        pass

    def setMenuBar(self, menu):
        self.menu = menu
    
    def setStatusBar(self, bar):
        pass
    
    def setWindowTitle(self, text):
        pass
    
    def close(self):
        pass
    
    def menuBar(self):
        return self.menu
    
    def addToolBar(self, toolbar):
        pass

# fake version        
QT_VERSION_STR = "1.0.0"

class QStatusBar():
    def __init__(self, window):
        pass
    
    def setObjectName(self, name):
        pass

class QMenu():
    def __init__(self):
        pass
    
    def addAction(self, action):
        pass
    
    def addSeparator(self):
        pass
    

class QMenuBar():
    def __init__(self, window):
        pass
    
    def setGeometry(self, rect):
        pass
    
    def setObjectName(self, name):
        pass
    
    def addMenu(self, entry):
        return QMenu()

    def addSeparator(self):
        pass
    
class QMessageBox():
    def __init__(self):
        pass
    
    @staticmethod
    def warning(obj, text1, text2, text3, options):
        pass

    Save = 0
    Cancel = 1
    
def QGraphicsScene():
    pass


QFileDialog = None
QTextEdit = None

class QAction():
    def __init__(self, window, param2=None, param3=None):
        pass
    
    def setIcon(self, Icon):
        pass

    def setObjectName(self, name):
        pass
    
    def setText(self, text):
        pass

    def setShortcut(self, param):
        pass

    def setStatusTip(self, text):
        pass
    
    
    class triggered():
        @staticmethod
        def connect(entry):
            pass
    
class QSizePolicy():
    def __init__(self, x, y):
        pass
    
    def setHorizontalStretch(self, param):
        pass
    
    def setVerticalStretch(self, param):
        pass
    
    def setHeightForWidth(self, param):
        pass
    
    def hasHeightForWidth(self):
        pass
    
    Expanding = 1

class QGraphicsView():
    def __init__(self, parent):
        print("Create QGraphicsView")

    def setTransformationAnchor(self, item):
        pass
    
    def AnchorUnderMouse(self):
        pass
    
    def setResizeAnchor(self, item):
        pass
    
    def setVerticalScrollBarPolicy(self, scroll_always):
        pass
    
    def setHorizontalScrollBarPolicy(self, x):
        print("QGraphicsView: setHorizontalScrollBarPolicy")

    def setFrameShape(self, x):
        print("QGraphicsView: setFrameShape")
    
    def sizePolicy(self):
        return QSizePolicy(1, 2)
    
    def setSizePolicy(self, policy):
        pass
    
    def setBaseSize(self, sizetype):
        pass
    
    def setAutoFillBackground(self, flag):
        pass
    
    def setBackgroundBrush(self, param):
        pass
    
    def setObjectName(self, name):
        pass
        
    
class QVBoxLayout():
    def __init__(self):
        print("Create QVBoxLayout")

    def setObjectName(self, name):
        print("QVBoxLayout Set object name")

    def addWidget(self, param):
        pass

    def addLayout(self, layout):
        pass
    
class QHBoxLayout():
    def __init__(self):
        print("Create QHBoxLayout")

    def setObjectName(self, name):
        print("QHBoxLayout Set object name")

    def addLayout(self, layout):
        pass
    
    def addWidget(self, item):
        pass
    
    def setStretch(self, x, y):
        pass
    
class QSpinBox():
    def __init__(self, widget):
        pass

    def setObjectName(self, name):
        print("QSpinBox Set object name")

    
class QGridLayout():
    def __init__(self, widget):
        print("Create QGridLayout")

    def setObjectName(self, name):
        print("QGridLayout Set object name")

    def addLayout(self, layout, x, y, x2, y2):
        pass
        
class QWidget():
    def __init__(self, window):
        print("Create QWidget")

    def setObjectName(self, name):
        print("QWidget Set object name")

class QSlider():
    def __init__(self, widget):
        pass
    
    def setOrientation(self, param):
        pass
    
    
    def setObjectName(self, name):
        pass
    
    
class QGraphicsItem():
    def __init__(self):
        pass
 
class QPushButton():
    def __init__(self, widget):
        pass
    
    def setObjectName(self, name):
        pass
    
    def setText(self, text):
        pass
    
    
    
class QCheckBox():
    def __init__(self, widget):
        pass
    
    def setObjectName(self, name):
        pass
    
    def setText(self, text):
        pass

    
class QLineEdit():
    def __init__(self, widget):
        pass
    
    def setText(self, text):
        pass
    
    def setObjectName(self, name):
        pass
    
    def setPlaceholderText(self, text):
        pass
    
    
class QListWidget():
    def __init__(self, widget):
        pass

    def setObjectName(self, name):
        pass
 
