from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QButtonGroup, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QSpinBox


menu_pushbutton = QPushButton("Меню")
pouse_continue_pushbutton = QPushButton("Пауза/Старт")
answer_pushbutton = QPushButton("Відповідь")

button1 = QRadioButton("1")
button2 = QRadioButton("2")
button3 = QRadioButton("3")
button4 = QRadioButton("4")

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


