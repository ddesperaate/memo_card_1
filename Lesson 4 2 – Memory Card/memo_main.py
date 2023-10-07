from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from random import shuffle


# import module second
from memo_card_layout import *

# crate main objects
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Memory Card")
card_width, card_height = 600, 500
main_window.resize(card_width, card_height)
main_window.move(50, 50)
            
        
# forms with answers
frm_question = "Яблуко"
frm_right = "apple"
frm_wrong1 = "application"
frm_wrong2 = "building"
frm_wrong3 = "catterpilar"

# create list
radio_list = [button1, button2, button3, button4]


# 
def check_result():
    correct = radio_list[0].isChecked()
    if correct:
        label_true_false.setText("Правильно")
        show_result()
    else:
        incorrect = radio_list[1].isChecked() or radio_list[2].isChecked() or
        radio_list[3].isChecked()
        if incorrect:
            label_true_false.setText("Не правильно")
            show_result()

def click_Ok(self):
    if label_true_false.text() != "Наступне питання":
        check_rusult()
    




# shuffle buttons
shuffle(radio_list)

# set text on buttons
radio_list[0].setText(frm_right)
radio_list[1].setText(frm_wrong1)
radio_list[2].setText(frm_wrong2)
radio_list[3].setText(frm_wrong3)

# blit right answer
answer1.setText(frm_right)

# while click button
answer_pushbutton.clicked.connect(show_result)


button.clicked.connect(click_Ok)

main_window.setLayout(mainvline)
main_window.show()
app.exec_()

