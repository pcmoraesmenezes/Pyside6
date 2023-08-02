from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from enviroments import MEDIUM_FONT_SIZE
from utility import isNumOrDot, isEmpty, isValidNumber
from typing import TYPE_CHECKING
import math
import operator


if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


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


class ButtonsGrid(QGridLayout):
    def __init__(
            self, display: 'Display', info: 'Info',
            window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._equationInitialValue = 'make a wish'
        self._left = None
        self._right = None
        self._op = None
        self.window = window

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):

        self.display.eqRequested.connect(lambda: print(123))

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(
                    self._insertButtonTextToDisplay,
                    button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
                )

        if text in '=':
            self._connectButtonClicked(button, self._eq)

        if text in '◀':
            self._connectButtonClicked(button, self.display.backspace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self,  button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Please type a number first')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Type the value(s)')
            return

        if self._left is None or self._op is None:
            self._showError('Incomplete equation')
            return

        self._right = float(displayText)
        # self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        # try:
        #     if '^' in self.equation and isinstance(self._left, float):
        #         result = math.pow(self._left, self._right)
        #     else:
        #         result = eval(self.equation)  # avalia string como código
        # except ZeroDivisionError:
        #     self._showError('Zero Division Error')
        # except OverflowError:
        #     self._showError('Stack Overflow')
        try:
            if self._op == '+':
                result = operator.add(self._left, self._right)
            elif self._op == '-':
                result = operator.sub(self._left, self._right)
            elif self._op == '*':
                result = operator.mul(self._left, self._right)
            elif self._op == '/':
                if self._right == 0:
                    self._showError('Zero Division Error')
                    return
                result = operator.truediv(self._left, self._right)
            elif self._op == '^':
                result = math.pow(float(self._left), self._right)
        except OverflowError:
            self._showError('Stack Overflow')
        self.display.clear()
        self.info.setText(f'{self._left} {self._op} {self._right} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Warning)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Ok
            # Para adicionar mais botões basta colocar o |
            # |
            # msgBox.StandardButton.Save
        )
        # E para obter o botão que o usuario pressionou basta:
        # result = msgBox.exec()
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
