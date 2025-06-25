from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QInputDialog,
    QFileDialog,
    QDialog,
)

from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QTimer, QFile, QSize
from PySide6.QtUiTools import QUiLoader

import numpy as np
import sys

from mainwindow_button_1 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("title here")

        
        self.ui.button.clicked.connect(self.on_button_clicked) # Making a button 

    def on_button_clicked(self): # Making a button 
        QMessageBox.information(self, "Button Clicked", "You clicked the button!")
        print("Button was clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())