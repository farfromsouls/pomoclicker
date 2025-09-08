from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)

from .data import *


class ShopWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PomoClicker")
        self.setFixedSize(400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)