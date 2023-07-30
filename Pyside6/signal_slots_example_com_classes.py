import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):  # Criando uma classe que herda de QMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('My beautiful window')

        button1 = self.make_button('Button1', 100)
        button1.clicked.connect(self.second_action_is_marked)  # type: ignore

        button2 = self.make_button('Button2', 50)

        button3 = self.make_button('Button3', 25)

        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(button3, 3, 1, 1, 2)
        self.grid_layout.addWidget(button1, 1, 1, 1, 1)
        self.grid_layout.addWidget(button2, 1, 2, 1, 1)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Show message in bar')

        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('First menu')
        self.first_action = self.first_menu.addAction('First action')
        self.first_action.triggered.connect(  # type: ignore
            self.Change_status_bar_name)

        self.seccond_action = self.first_menu.addAction('Seccond action')
        self.seccond_action.setCheckable(True)
        self.seccond_action.toggled.connect(   # type: ignore
           self.second_action_is_marked)
        self.seccond_action.hovered.connect(   # type:ignore
           self.second_action_is_marked)

    @Slot()
    def Change_status_bar_name(self):
        self.status_bar.showMessage('Slot is executed')

    @Slot()
    def second_action_is_marked(self):
        print('Is marked? ', self.seccond_action.isChecked())

    def make_button(self, text, textize):
        button = QPushButton(text)
        button.setStyleSheet(f'font-size: {textize}px')
        print(f'Created button: {text}, font-size: {textize}px')
        return button


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print('Application initialized')
    window = MyWindow()
    app.setActiveWindow(window)  # Adiciona a janela principal ao aplicativo
    window.resize(500, 300)
    window.show()
    app.exec()
