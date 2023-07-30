# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget
                               )
app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('A title for a window')

button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px; color: red;')

button2 = QPushButton('New button text')
button2.setStyleSheet('font-size: 24px; color: green;')

button3 = QPushButton('Adding a new button')
button3.setStyleSheet('font-size:36px; color: blue;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

# Two blank lines before the function


def slot_example(status_bar):

    status_bar.showMessage('The slot is executed')


status_bar = window.statusBar()
status_bar.showMessage('Show message in bar')

menu = window.menuBar()
first_menu = menu.addMenu('First menu')
first_action = first_menu.addAction('First action')
first_action.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
)

window.show()
app.exec()
