import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__() 

        # Window settings
        self.setWindowTitle("Special Midterm Exam in OOP")
        self.setGeometry(300, 300, 300, 300)
        self.setWindowIcon(QIcon('pythonico.ico')) 

        # Create the button
        self.button = QPushButton('Click to change color', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 100)
        self.button.clicked.connect(self.on_click)  

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.button.setStyleSheet("background-color: yellow")
        print("Color Changed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
