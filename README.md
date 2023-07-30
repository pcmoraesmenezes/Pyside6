<h1 align="center"> PySide6 </h1>
    ![githubbanner](https://github.com/pcmoraesmenezes/Pyside6/assets/105931834/5c085a68-4994-44b2-a517-74c1bd85f9d0)

 Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
  - Qt é uma biblioteca usada para a criação de GUI (interface gráfica
    do usuário) escrita em C++.
    - PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a
    biblioteca para a criação de interfaces gráficas sem ter que usar outra

  - PySide6 é uma referencia à versão 6 da Qt (Qt 6)
  - Qt é multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

 - PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do
    projeto Qt for Python project - https://doc.qt.io/qtforpython/
  - Por usarem a mesma biblioteca (Qt), PySide e PyQt são extremamente
    similares, muitas vezes os códigos são idênticos. Portanto, mesmo que você
    ainda queira usar PyQt, será muito simples portar os códigos. Muitas vezes
    basta trocar o nome de PySide para PyQt e vice-versa.
  - A maior diferença entre PyQt e PySide está na licença:
    PyQt usa GPL ou commercial e PySide usa LGPL.
    Em resumo: com PySide, você tem a permissão uso da biblioteca para fins
    comerciais, sem ter que compartilhar o código escrito por você para o
    público.
    Licenças são tópicos complexos, portanto, se oriente sobre elas
    antes de usar qualquer software de terceiros.
    https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)

 QApplication e QPushButton de PySide6.QtWidgets
  QApplication -> O Widget principal da aplicação
  QPushButton -> Um botão
  PySide6.QtWidgets -> Onde estão os widgets do PySide6

 QWidget e QLayout de PySide6.QtWidgets
  QWidget -> genérico
  QLayout -> Um widget de layout que recebe outros widgets

<h2 align="center"> Explicação do código signal_slots_example.py </h2>

<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>
