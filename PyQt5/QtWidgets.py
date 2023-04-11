'''
Created on 5 Apr 2023

@author: Rob Probin
'''
from PyQt5.QtCore import QRect, pyqtSignal
import inspect
import asyncio
import pygame

_last_app_instance = None

class QApplication():
    '''
    Fake QApplication
    '''

    def __init__(self, args):
        '''
        Constructor
        '''
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {args}")
        print("We could process args here")
        self._screen_width = 640
        self._screen_height = 480
        
        #
        global _last_app_instance
        _last_app_instance = self
    
      
    def resize(self, screen_width, screen_height):
        ''' doesn't resize the window at the moment '''
        self._screen_width = screen_width
        self._screen_height = screen_height

        
    async def _pygame_loop(self):
        pygame.init()
        
        our_flags = pygame.RESIZABLE
        screen = pygame.display.set_mode((self._screen_width, self._screen_height), flags = our_flags)
        clock = pygame.time.Clock()
    
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
            # Your game logic and drawing code here
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), [100, 100], 10)
            pygame.display.flip()
            #pygame.display.update()
            print( pygame.display.get_window_size())
            # required for 
            await asyncio.sleep(0)  # Very important, and keep it 0
            # Sleep for a short duration to allow other tasks to run
            #await asyncio.sleep(1/60)  # Cap the frame rate at 60 FPS
    
            # Update the clock, limit the frame rate to 60
            clock.tick(60)
    
        pygame.quit()

    async def _main(self):
        # Schedule other async tasks here if needed
        await self._pygame_loop()
    
    def exec_(self):
        error = 0
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
        
        print("main loop for QT application goes here :-)")
        asyncio.run(self._main())
    
        return error
    
    
class QFrame():
    NoFrame = 1
    HLine = 2
    Sunken = 3
      
    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")
    
    def setFrameShape(self, xtype):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {xtype}")
    
    def setFrameShadow(self, xtype):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {xtype}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")


class QLabel():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")

    def setFont(self, font):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {font}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def setTextFormat(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def setText(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")


class QToolBar():

    def __init__(self, toolbar):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {toolbar}")
    
    def addAction(self, action):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {action}")
    
    
class QMainWindow():

    def __init__(self):
        self.menu = None
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def resize(self, screen_width, screen_height):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {screen_width} {screen_height}")
        if _last_app_instance is not None:
            _last_app_instance.resize(screen_width, screen_height)
            
    @staticmethod
    def setWindowIcon(icon):
        print("QMainWindow::setWindowIcon")
        
    def setVerticalScrollBarPolicy(self, x):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x}")

    def setHorizontalScrollBarPolicy(self, x):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x}")
    
    def setCentralWidget(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")

    def setMenuBar(self, menu):
        self.menu = menu
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {menu}")
    
    def setStatusBar(self, bar):
        self.status_bar = bar
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {bar}")

    def statusBar(self):
        return self.status_bar
    
    def setWindowTitle(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")
    
    def close(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    def menuBar(self):
        return self.menu
    
    def addToolBar(self, toolbar):
        return QToolBar(toolbar)

    def setWindowModified(self, state):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {state}")
    
    def show(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")


# fake version        
QT_VERSION_STR = "1.0.0"


class QStatusBar():

    def __init__(self, window):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {window}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")

    def showMessage(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")


class QMenu():

    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    def addAction(self, action):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {action}")
    
    def addSeparator(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    

class QMenuBar():

    def __init__(self, window):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {window}")
    
    def setGeometry(self, rect):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {rect}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def addMenu(self, entry):
        return QMenu()

    def addSeparator(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")

    
class QMessageBox():

    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    @staticmethod
    def warning(obj, text1, text2, text3, options):
        print("QMessageBox::warning", obj, text1, text2, text3, options)

    Save = 0
    Cancel = 1


class _internal_scene():

    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    def addItem(self, item):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {item}")

    def sceneRect(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
        return QRect(1, 1, 10, 10)


def QGraphicsScene():
    return _internal_scene()


QFileDialog = None
QTextEdit = None


class QAction():

    def __init__(self, window, param2=None, param3=None):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    def setIcon(self, Icon):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {Icon}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def setText(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")

    def setShortcut(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")

    def setStatusTip(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")
    
    class triggered():

        @staticmethod
        def connect(entry):
            print("triggered::connect")

    
class QSizePolicy():

    def __init__(self, x, y):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x} {y}")
    
    def setHorizontalStretch(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def setVerticalStretch(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def setHeightForWidth(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def hasHeightForWidth(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    Expanding = 1


class QGraphicsView():

    def __init__(self, parent):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {parent}")

    def setTransformationAnchor(self, item):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {item}")
    
    def AnchorUnderMouse(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
    
    def setResizeAnchor(self, item):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {item}")
    
    def setVerticalScrollBarPolicy(self, scroll_always):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {scroll_always}")
    
    def setHorizontalScrollBarPolicy(self, x):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x}")

    def setFrameShape(self, x):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x}")
    
    def sizePolicy(self):
        return QSizePolicy(1, 2)
    
    def setSizePolicy(self, policy):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {policy}")
    
    def setBaseSize(self, sizetype):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {sizetype}")
    
    def setAutoFillBackground(self, flag):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {flag}")
    
    def setBackgroundBrush(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
        
    def setScene(self, scene):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {scene}")
    
    def fitInView(self, view):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {view}")
    
    def update(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")

    
class QVBoxLayout():

    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")

    def addWidget(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")

    def addLayout(self, layout):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {layout}")

    
class QHBoxLayout():

    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")

    def addLayout(self, layout):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {layout}")
    
    def addWidget(self, item):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {item}")
    
    def setStretch(self, x, y):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x} {y}")

    
class QSpinBox():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")

    
class QGridLayout():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")

    def addLayout(self, layout, x, y, x2, y2):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {x} {y} {x2} {y2}")

        
class QWidget():

    def __init__(self, window):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {window}")

    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")


class QSlider():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")
    
    def setOrientation(self, param):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {param}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    
class QGraphicsItem():

    def __init__(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")

    def setScene(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
        
    def update(self):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name}")
        
 
class QPushButton():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def setText(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")
    
    
class QCheckBox():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")
        self.stateChanged = pyqtSignal()
        
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def setText(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")

    def setChecked(self, state):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {state}")

    
class QLineEdit():

    def __init__(self, widget):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {widget}")
        self.textChanged = pyqtSignal()
        
    def setText(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")
    
    def setObjectName(self, name):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {name}")
    
    def setPlaceholderText(self, text):
        current_class_name = self.__class__.__name__
        current_method_name = inspect.currentframe().f_code.co_name
        print(f"Current class: {current_class_name}, Current method: {current_method_name} {text}")
    


class _QListWidget_text():

    def __init__(self, text):
        self._text = text

    def text(self):
        return self._text


    
class QListWidget():
# No GUI yet, just datastorage
    def __init__(self, widget):
        self.list_data = [] 
        self.name = "QListWidget"
        self.current_row = 0
        self.currentItemChanged = pyqtSignal()

    def setObjectName(self, name):
        self.name = name
        
    def clear(self):
        self.list_data = [] 
        self.current_row = 0
    
    def addItem(self, text):
        obj = _QListWidget_text(text)
        self.list_data.append(obj)
    
    def setCurrentRow(self, row_num):
        self.current_row = row_num
        
    def currentItem(self):
        return self.list_data[self.current_row]

