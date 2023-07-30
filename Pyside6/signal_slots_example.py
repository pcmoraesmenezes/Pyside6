import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()

window.setCentralWidget(central_widget)
window.setWindowTitle('My beautiful window')

button1 = QPushButton('Button text')
button1.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('Slot is executed')
    return inner


@Slot()
def other_slot(checked):
    print('Is marked? ', checked)


@Slot()
def thirty_slot(action):
    def inner():
        other_slot(action.isChecked())
    return inner


status_bar = window.statusBar()
status_bar.showMessage('Show message in bar')

menu = window.menuBar()
first_menu = menu.addMenu('First menu')
first_action = first_menu.addAction('First action')
first_action.triggered.connect(slot_example(status_bar))  # type: ignore

seccond_action = first_menu.addAction('Seccond action')
seccond_action.setCheckable(True)
seccond_action.toggled.connect(other_slot)  # type: ignore
seccond_action.hovered.connect(thirty_slot(seccond_action))  # type:ignore

button1.clicked.connect(thirty_slot(seccond_action))  # type: ignore

window.show()
app.exec()
