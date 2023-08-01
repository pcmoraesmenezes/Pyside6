from PySide6.QtWidgets import QApplication
from display import Display

# from PySide6.QtWidgets import QVBoxLayout
from main_window import MainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    # Define o ícone da aplicação
    window.set_icon_app()

    # Display
    display = Display()
    # display.setPlaceholderText('Digite algo')  # Apaga esse conteudo quando
    # o usuario digita algo
    window.addToVLayout(display)
    window.addToVLayout(Display('Display 1'))
    window.addToVLayout(Display('Display 2'))

    window.adjustFixedSize()
    window.show()
    app.exec()
