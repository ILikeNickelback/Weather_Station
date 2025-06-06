import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QLCDNumber, QGraphicsView, QGraphicsScene, QMainWindow, QVBoxLayout, QWidget, QTabWidget

from PyQt5 import uic
import qdarkstyle

from appfunctions import appFunctions
from dataSimulation import dataSimulation
from graphFunctions import graphFunctions




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
        self.dataSimulation = dataSimulation()
        self.graphFunctions = graphFunctions(self)
        self.appFunctions = appFunctions(self)

        
        self.carbonScale = self.findChild(QWidget, 'carbonScale')
        layout = QVBoxLayout(self.carbonScale)
        layout.addWidget(self.graphFunctions)
        
        
    def setup_ui(self):
        uic.loadUi('C:/Users/Christopher/Desktop/Weather_Sation/WeatherStation.ui', self)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        
        
    def assign_buttons(self):
        self.motivationButton.clicked.connect(self.on_push_button_clicked)
        self.realisteButton.clicked.connect(self.on_push_button_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
