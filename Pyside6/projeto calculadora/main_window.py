from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PySide6.QtWidgets import QVBoxLayout


from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
