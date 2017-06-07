from PySide import*
from PySide.QtCore import*
from PySide.QtGui import*

class Elements:
    pass

class MainWindow(QWidget):
    def __init__(self, controller):
        self.controller = controller
        super(MainWindow, self).__init__()
        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
    
    def addWidget(self, widget):
        self.layout.addWidget(widget)
        return widget