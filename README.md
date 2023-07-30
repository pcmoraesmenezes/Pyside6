<h1 align="center"> PySide6 </h1>
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

<h2>Algumas explicações e termos </h2>
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

## ✔️ Técnicas e tecnologias utilizadas

As técnicas e tecnologias utilizadas pra isso são:
- `Python 3`
- `Pyside6`
  
# :hammer: Funcionalidades do projeto
- `Explicação do código signal_slots_example.py`: 
<br>
Árquivo contendo a explicação pode ser encontrado nesse link: https://github.com/pcmoraesmenezes/Pyside6/blob/main/explica%C3%A7%C3%B5es/explica%C3%A7%C3%A3o_signal_slots_example

## 📁 Acesso ao projeto
Você pode [acessar os codigos do projeto aqui](https://github.com/pcmoraesmenezes/Pyside6.git)

## 🛠️ Abrir e rodar o projeto
Para executar os códigos é necessário a biblioteca PySide6, para isso você pode dar um pip install PySide6. Recomenda-se o uso do venv, pois a biblioteca do PySide6 é relativamente grande

<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>
