import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QLCDNumber, QGraphicsView, QGraphicsScene, QMainWindow, QVBoxLayout, QWidget, QTabWidget

from PyQt5 import uic
import qdarkstyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        uic.loadUi('C:/Users/Christopher/Desktop/Weather_Sation/WeatherStation.ui', self)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
