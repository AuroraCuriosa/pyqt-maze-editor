'''
Created on 5 Apr 2023

@author: Rob Probin
'''

class QApplication():
    '''
    Fake QApplication
    '''


    def __init__(self, args):
        '''
        Constructor
        '''
        pass
    
    
class QMainWindow():
    def __init__(self):
        pass
    
    
# fake version        
QT_VERSION_STR = "1.0.0"


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
QMainWindow = None
QTextEdit = None
QTextEdit = None
QAction = None
QWidget = None 
