from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton


# import module second
from memo_card_layout import *

# crate main objects
app = QApplication([])
question_window = QWidget()
question_window.setWindowTitle("Memory Card")
qcard_width, qcard_height = 600, 700
question_window.resize(card_width, card_height)
question_window.move(150, 150)
            
