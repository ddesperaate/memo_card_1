from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from random import shuffle
from random import choice
from PyQt5.QtCore import QTimer
time_unit = 60000 # one minute
timer = QTimer


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



frm_question = one_qlineedit.text()
frm_right = two_qlineedit.text()
frm_wrong1 = three_qlineedit.text()
frm_wrong2 = four_qlineedit.text()
frm_wrong3 = five_qlineedit.text()

# forms with answers
# считывание информации
def create_question():
    frm_question = one_qlineedit.text()
    frm_right = two_qlineedit.text()
    frm_wrong1 = three_qlineedit.text()
    frm_wrong2 = four_qlineedit.text()
    frm_wrong3 = five_qlineedit.text()

    q = Question(frm_question, frm_right, frm_wrong1, frm_wrong2, frm_wrong3)
    question_list.append(q)


def crear_qlineedit():
    one_qlineedit.clear()
    two_qlineedit.clear()
    three_qlineedit.clear()
    four_qlineedit.clear()
    five_qlineedit.clear()



def start_answer():
    random_question = choice(question_list)
    # set text on buttons
    radio_list[0].setText(random_question.answer)
    radio_list[1].setText(random_question.wrong_answer1)
    radio_list[2].setText(random_question.wrong_answer2)
    radio_list[3].setText(random_question.wrong_answer3)
    question_widget.setText(random_question.question)
    # правил.вариант.setText(random_question.answer)


def sleep():
    main_window.hide()
    boxtime = box_minutes.text()
    int(boxtime)
    timer.setInterval(boxtime * time_unit)


def wakeup():
    


# shuffle buttons
shuffle(radio_list)



# blit right answer
answer1.setText(frm_right)

# while click button
answer_pushbutton.clicked.connect(click_Ok)

next_pushbutton.clicked.connect(create_question)

clear_pushbutton.clicked.connect(crear_qlineedit)

next_pushbutton.clicked.connect(start_answer)




main_window.setLayout(mainvline)

# set zero_main_vline on question_window
question_window.setLayout(zero_main_vline)
question_window.show()
main_window.show()
app.exec_()

