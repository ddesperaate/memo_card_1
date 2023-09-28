from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

# crate main objects
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Memory Card")
card_width, card_height = 600, 500
main_window.resize(card_width, card_height)
main_window.move(50, 50)



main_window.show()
app.exec_()


