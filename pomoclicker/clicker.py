from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMainWindow
from .data import *
from .styles import *


class ClickerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clicker!@")
        self.setFixedSize(400, 300)
        self.setStyleSheet(stats_style)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setSpacing(0)