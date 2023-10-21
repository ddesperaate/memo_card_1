from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from random import shuffle


# import module second
from memo_card_layout import *
from memo_question_layout import *

# crate main objects
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Memory Card")
card_width, card_height = 600, 500
main_window.resize(card_width, card_height)
main_window.move(50, 50)
            
        


# create list
radio_list = [button1, button2, button3, button4]


# 
def check_result():
    correct = radio_list[0].isChecked()
    if correct:
        label_true_false.setText("Правильно")
        show_result()
    else:
        incorrect = radio_list[1].isChecked() or radio_list[2].isChecked() or radio_list[3].isChecked()
        if incorrect:
            label_true_false.setText("Не правильно")
            show_result()

def click_Ok(self):
    if label_true_false.text() == "Наступне питання":
        check_rusult()

# list questions
question_list = []


# forms with answers
def create_question():
    frm_question = one_qlineedit.text()
    frm_right = two_qlineedit.text()
    frm_wrong1 = three_qlineedit.text()
    frm_wrong2 = four_qlineedit.text()
    frm_wrong3 = five_qlineedit.text()

    q = Question(frm_question, frm_right, frm_wrong1, frm_wrong2, frm_wrong3)
    question_list.append(q)



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
answer_pushbutton.clicked.connect(click_Ok)

next_pushbutton.clicked.connect(create_question)




main_window.setLayout(mainvline)

# set zero_main_vline on question_window
question_window.setLayout(zero_main_vline)
#question_window.show()
main_window.show()
app.exec_()

