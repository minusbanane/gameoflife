from PySide import*
from PySide.QtCore import*
from PySide.QtGui import*
from model import Model
app = QApplication([])

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QBoxLayout(QBoxLayout.TopToBottom, self)

        model = Model()
        model.dimensions = [2,5]
        print(model.dimensions)

window = MainWindow()
window.show()
app.exec_()