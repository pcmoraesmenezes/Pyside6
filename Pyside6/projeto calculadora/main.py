from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PySide6.QtWidgets import QVBoxLayout
from main_window import MainWindow

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()

    central_widget = QWidget()
    v_layout = QVBoxLayout()
    central_widget.setLayout(v_layout)

    label1 = QLabel('My text')
    v_layout.addWidget(label1)

    window.setCentralWidget(central_widget)
    window.show()

    app.exec()
