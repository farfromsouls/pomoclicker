from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
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
        layout.setSpacing(0)

        self.clicks = getClicks()

        clickLayout = QVBoxLayout()
        self.clickLabel = QLabel(f"{self.clicks}")
        clickButton = QPushButton()
        clickLayout.addWidget(self.clickLabel)
        clickLayout.addWidget(clickButton)

        clickButton.clicked.connect(self.__Click)

        layout.addLayout(clickLayout)

    def __Click(self):
        addClicks(1)
        self.clicks = self.clicks + 1
        self.clickLabel.setText(f"{self.clicks}")