from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

# import module second
from memo_card_layout import *

# crate main objects
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Memory Card")
card_width, card_height = 600, 500
main_window.resize(card_width, card_height)
main_window.move(50, 50)


# while click button
answer_pushbutton.clicked.connect(show_result)


main_window.setLayout(mainvline)
main_window.show()
app.exec_()



