from PySide import*
from PySide.QtCore import*
from PySide.QtGui import*

from Views import MainWindow
from Views import Elements
from Models import Grid

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def store_height(self, height):
        self.model.grid.dimensions = [self.model.grid.dimensions[0], height]
        self.view.log(self.model.grid.dimensions)

    def store_width(self, width):
        self.model.grid.dimensions = [width, self.model.grid.dimensions[1]]
        self.view.log(self.model.grid.dimensions)

    def start_page(self):
        self.view.start_page()
        self.view.render()
    
    def start_game(self):
        self.view.log('Game starting...')

class Model:
    def __init__(self):
        self.grid = Grid()

class View:
    def __init__(self, controller):
        self.app = QApplication([])
        self.controller = controller
        self.window = MainWindow(controller)
        self.elements = Elements()

    def start_page(self):
        self.window.setWindowTitle('Start - Game Of Life')

        self.elements.height_label = self.window.addWidget(QLabel('Höhe des Spielfeldes'))
        self.elements.height_input = self.window.addWidget(QSpinBox())
        self.elements.width_label = self.window.addWidget(QLabel('Breite des Spielfeldes'))
        self.elements.width_input = self.window.addWidget(QSpinBox())
        self.elements.start_button = self.window.addWidget(QPushButton('Starten'))

        self.elements.width_input.setValue(self.controller.model.grid.dimensions[0])
        self.elements.height_input.setValue(self.controller.model.grid.dimensions[1])

        self.elements.start_button.clicked.connect(self.controller.start_game)
        self.elements.height_input.valueChanged.connect(self.controller.store_height)
        self.elements.width_input.valueChanged.connect(self.controller.store_width)

    def render(self):
        self.window.show()
        self.app.exec_()

    def log(self, arg):
        print(arg)