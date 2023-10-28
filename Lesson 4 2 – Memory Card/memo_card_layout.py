from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit


# crate main objects

question_window = QWidget()
question_window.setWindowTitle("Question Card")
qcard_width, qcard_height = 600, 350
question_window.resize(qcard_width, qcard_height)
question_window.move(150, 150)

# vertical lines
zero_main_vline = QVBoxLayout()
one_vline = QVBoxLayout()
two_vline = QVBoxLayout()

# horizont lines
one_hline = QHBoxLayout()
two_hline = QHBoxLayout()
three_hline = QHBoxLayout()

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
one_vline.addWidget(one_label)
one_vline.addWidget(two_label)
one_vline.addWidget(three_label)
one_vline.addWidget(four_label)
one_vline.addWidget(five_label)

# add QLineEdits to two_hline
two_vline.addWidget(one_qlineedit)
two_vline.addWidget(two_qlineedit)
two_vline.addWidget(three_qlineedit)
two_vline.addWidget(four_qlineedit)
two_vline.addWidget(five_qlineedit)


# add one_vline and two_vline to one_hline
one_hline.addLayout(one_vline)
one_hline.addLayout(two_vline)

# add pushbuttons to two_hline
two_hline.addWidget(add_question_pushbutton)
two_hline.addWidget(clear_pushbutton)
# add next_pushbutton to third hline
three_hline.addWidget(next_pushbutton)

# add one_hline and two_hline to zero_main_vline
zero_main_vline.addLayout(one_hline)
zero_main_vline.addLayout(two_hline)
zero_main_vline.addWidget(next_pushbutton)




class Question():
    def __init__ (self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        #конструктор класу
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attempts = 0 # Переменная для всез ответов
        self.correct = 0 # Переменная для подсчёта правльных ответов
    

    def got_right(self):
        print("Це правильна відповідь!")
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        print("Відповідь невірна")
        self.attempts += 1
