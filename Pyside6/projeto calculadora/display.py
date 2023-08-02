from PySide6.QtWidgets import QLineEdit
from enviroments import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent


class Display(QLineEdit):
    eqRequested = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # Usa uma list compreenshion para dar um espaço extra no canto direito
        # Ao invés de ele pegar um text_margin e passar quatro vezes, pois sãõ
        # 4 parametros, faz-se uso de um for para aplicar os quatro parametros
        # unicamente
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        # ALinha o texto a direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]

        if isEnter:
            print('Enter pressed, signal emited', type(self).__name__)
            self.eqRequested.emit()
            return event.ignore()
        # return super().keyPressEvent(event)
