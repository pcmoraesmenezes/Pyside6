from PySide6.QtWidgets import QPushButton
from enviroments import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setItalic(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')
