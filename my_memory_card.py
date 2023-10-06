#создай приложение для запоминания информации
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton, QButtonGroup,
        QPushButton, QLabel
    )
from random import randint, shuffle, choice

#Класс для создания вопросов
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

que_list = []
que_list.append(Question('Какой национальности не существует?', 'смурфы', 'алеуты', 'чулымцы', 'энцы'))
que_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'ИСпанский', 'Итальянский', 'Бразильский'))
que_list.append(Question('Как на польском холм?', 'pagorek', 'a', 'b', 'c'))
que_list.append(Question('Как на польском город?', 'miasto', 'a', 'b', 'c'))

app = QApplication([])
b_Ok = QPushButton('Ответить!')
lb_que = QLabel('Самый вопрос')

#Варианты ответов
rad_gr_box = QGroupBox('Варианты ответов')

q1 = QRadioButton('Вариант ответа1')
q2 = QRadioButton('Вариант ответа2')
q3 = QRadioButton('Вариант ответа3')
q4 = QRadioButton('Вариант ответа4')

rad_gr = QButtonGroup()

rad_gr.addButton(q1)
rad_gr.addButton(q2)
rad_gr.addButton(q3)
rad_gr.addButton(q4)

aI = QHBoxLayout()
aT1 = QVBoxLayout()
aT2 = QVBoxLayout()

#расположение виджетов по лэйаутам

aT1.addWidget(q1)
aT1.addWidget(q2)
aT2.addWidget(q3)
aT2.addWidget(q4)

aI.addLayout(aT1)
aI.addLayout(aT2)
rad_gr_box.setLayout(aI)

'''результат теста'''
ans_gr_box = QGroupBox('Результаты теста')
lb_res = QLabel('прав\нет')
lb_cor = QLabel('Ответ тут')

rT1 = QVBoxLayout()
rT1.addWidget(lb_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
rT1.addWidget(lb_cor, alignment=Qt.AlignCenter, stretch = 2)
ans_gr_box.setLayout(rT1)

#виджеты

I1 = QHBoxLayout()
I2 = QHBoxLayout()
I3 = QHBoxLayout()

I1.addWidget(lb_que, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
I2.addWidget(rad_gr_box)
I2.addWidget(ans_gr_box)
ans_gr_box.hide()

I3.addStretch(1)
I3.addWidget(b_Ok, stretch = 2)
I3.addStretch(1)

T1 = QVBoxLayout()

T1.addStretch(1)
T1.addLayout(I1, stretch = 2)
T1.addStretch(1)
T1.addLayout(I2, stretch = 8)
T1.addStretch(1)
T1.addLayout(I3, stretch = 1)
T1.addStretch(1)
T1.addSpacing(5)

#функции
ans = [q1, q2, q3, q4]

def show_que():
    rad_gr_box.show()
    ans_gr_box.hide()
    b_Ok.setText('Ответить')
    rad_gr.setExclusive(False)
    q1.setChecked(False)
    q2.setChecked(False)
    q3.setChecked(False)
    q4.setChecked(False)
    rad_gr.setExclusive(True)

def show_res():
    rad_gr_box.hide()
    ans_gr_box.show()
    b_Ok.setText('Следующий вопрос')

def ask(q: Question):
    shuffle(ans)
    ans[0].setText(q.right)
    ans[1].setText(q.wrong1)
    ans[2].setText(q.wrong2)
    ans[3].setText(q.wrong3)
    lb_que.setText(q.question)
    lb_cor.setText(q.right)

def show_cor(res):
    lb_res.setText(res)
    show_res()

def chek_ans():
    if ans[0].isChecked():
        show_cor('Правильно!')
    else:
        show_cor('Неверно!')

def next_que():
    q = choice(que_list)
    ask(q)

def click_Ok():
    if b_Ok.text() == 'Ответить!':
        chek_ans()
    elif b_Ok.text() == 'Следующий вопрос':
        next_que()

#создание приложения и главного окна

window = QWidget()
window.setLayout(T1)
window.setWindowTitle('Memory Card')

b_Ok.clicked.connect(click_Ok)
next_que()
window.resize(400, 300)
window.show()

app.exec_()