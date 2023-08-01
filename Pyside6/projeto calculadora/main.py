from PySide6.QtWidgets import QApplication
from display import Display
from info import Info
# from PySide6.QtWidgets import QVBoxLayout
from main_window import MainWindow
import sys
from styles import setupTheme
from buttons import Button


if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone da aplicação
    window.set_icon_app()

    info = Info('2.10 ^ 10.0 = 1024.0')
    window.addToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText('Digite algo')  # Apaga esse conteudo quando
    # o usuario digita algo
    window.addToVLayout(display)

    # Button
    button = Button('Button text')
    window.addToVLayout(button)
    button1 = Button('Button text')
    window.addToVLayout(button1)
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
