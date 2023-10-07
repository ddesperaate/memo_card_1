from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

menu_pushbutton = QPushButton("Меню")
pouse_continue_pushbutton = QPushButton("Пауза/Старт")
answer_pushbutton = QPushButton("Відповідь")

button1 = QRadioButton("1")
button2 = QRadioButton("2")
button3 = QRadioButton("3")
button4 = QRadioButton("4")

# create main vert line
mainvline = QVBoxLayout()

# Об'єднання радіобаттонів у одну групу
RadioGroupBox = QGroupBox("Варіанти відповідей")

# Рамка для групи перемекичів з відповідями
RadioGroup = QButtonGroup()

RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

#spin_button
box_minutes = QSpinBox()
box_minutes.setValue(30)

# create two vertical line
vert_line_left = QVBoxLayout()
vert_line_right = QVBoxLayout()

# add four radiobutton on two vertical line
vert_line_left.addWidget(button1)
vert_line_left.addWidget(button2)
vert_line_right.addWidget(button3)
vert_line_right.addWidget(button4)

dop_hline = QHBoxLayout()
dop_hline.addLayout(vert_line_left)
dop_hline.addLayout(vert_line_right)
dop_hline.setLayoyt(RadioGroupBox)








# Horizont line
horizont_line1 = QHBoxLayout()
horizont_line1.addWidget(menu_pushbutton)
horizont_line1.addWidget(pouse_continue_pushbutton)
horizont_line1.addWidget(box_minutes)
minutes_left = QLabel("хвилин")
horizont_line1.addWidget(minutes_left)

# second H line
horizont_line2 = QHBoxLayout()
question = QLabel("Apple")
horizont_line2.addWidget(question)

# third H line
horizont_line3 = QHBoxLayout()
horizont_line3.addWidget(RadioGroupBox)
RadioGroup.setLayout(horizont_line3)

# fourth H line
horizont_line4 = QHBoxLayout()
horizont_line4.addWidget(answer_pushbutton)



# ---------- New Online Lesson 1 ----------

# ----- Box 2 with answers
box2 = QGroupBox("Результат теста")

label_true_false = QLabel(" idk ")
answer1 = QLabel(" ")#apple

v_res = QVBoxLayout()
v_res.addWidget(label_true_false, alignment = (Qt.AlignTop| Qt.AlignLeft))
v_res.addWidget(answer1, alignment = Qt.AlignCenter, stretch = 2)
box2.setLayout(v_res)

horizont_line3.addWidget(box2)
box2.hide()

def show_result(): #while push button - answer_pushbutton
    RadioGroupBox.hide()
    box2.show()
    answer_pushbutton.setText("Наступне питання")

def show_question():
    RadioGroupBox.show()
    answer_pushbutton.hide()



    

