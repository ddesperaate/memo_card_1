from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit


# crate main objects
app = QApplication([])
question_window = QWidget()
question_window.setWindowTitle("Question Card")
qcard_width, qcard_height = 600, 700
question_window.resize(qcard_width, qcard_height)
question_window.move(150, 150)

# vertical lines
zero_main_vline = QVBoxLayout()
one_vline = QVBoxLayout()
tow_vline = QVBoxLayout()

# horizont lines
one_hline = QHBoxLayout()
two_hline = QHBoxLayout()

# create labels
one_label = QLabel("Введіть запитання")
two_label = QLabel("Введіть вірну відповідь")
three_label = QLabel("Введіть першу хибну відповідь")
four_label = QLabel("Введіть другу хибну відповідь")
five_label = QLabel("Введіть третю хибну відповідь")

# create QLineEdit
one_qlineedit = QLineEdit()
two_qlineedit = QLineEdit()
three_qlineedit = QLineEdit()
four_qlineedit = QLineEdit()
five_qlineedit = QLineEdit()

# create pushbuttons
add_question_pushbutton = QPushButton("Додати запитання")
clear_pushbutton = QPushButton("Очистити")
next_pushbutton = QPushButton("Далі")


#---------------------------------------------------------
# add labels to one_hline
one_vline.addLayout(one_label)
one_vline.addLayout(two_label)
one_vline.addLayout(three_label)
one_vline.addLayout(four_label)
one_vline.addLayout(five_label)
# add QLineEdits to two_hline
two_vline.addLayout(one_qlineedit)
two_vline.addLayout(two_qlineedit)
two_vline.addLayout(three_qlineedit)
two_vline.addLayout(four_qlineedit)
two_vline.addLayout(five_qlineedit)

# add one_vline and two_vline to one_hline
one_hline.addLayout(one_vline)
one_hline.addLauout(two_vline)
# add pushbuttons to two_hline
two_hline.addWidget(add_question_pushbutton)
two_hline.addWidget(clear_pushbutton)

# add one_hline and two_hline to zero_main_vline
zero_main_vline.addLayout(one_hline)
zero_main_vline.addLayout(two_hline)


# set zero_main_vline on question_window
question_window.setLayout(zero_main_vline)
