#  Widgets são tudo que está na tela
#  As bibliotecas desse modulo lidará especificadamente com classes

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout
# from PySide6.QtWidgets import QVBoxLayout
import sys

app = QApplication(sys.argv)  # passar argumentos aqui é opcional porque
#  o metodo  contém @overload

#  Criando um botão
button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px; color: red;')

button2 = QPushButton('New button text')
button2.setStyleSheet('font-size: 24px; color: green;')

button3 = QPushButton('Adding a new button')
button3.setStyleSheet('font-size:36px; color: blue;')

# button.show()

#  Central widget é um widget genérico que so serve para ser o local central
#  Onde se colocará outros widgets, mas o central widget não recebe outros
#  widgets
central_widget = QWidget()


#  Para se receber outros widgets cria-se então um layout
# layout = QVBoxLayout()  # Adiciona verticalmente
layout = QGridLayout()  # Com essa classe, podemos definir a posição que
#  desejamos para a nossa aplicação
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)  # Row 1; Column 1
layout.addWidget(button2, 1, 2, 1, 1)  # Row 1; COlumn 2
layout.addWidget(button3, 3, 1, 1, 2)  # Row 3; column 1
#  Os numeros após a linha e coluna, indicam quantas linhas e quantas colunas
#  a aplicação irá preencher, note que se removermos essa aplicação do botão3
#  De certo modo o código ficaria desconexo, iria sobrar espaço na coluna para
#  o botão 3, então fazemos ele preencher duas colunas para contornar isso


central_widget.show()
app.exec()  # Loop da aplicação - deixa a janela ser executada até ser fechada
