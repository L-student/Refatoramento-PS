import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel


class window2(QMainWindow):
    def __ini__(self):
        super().__init__()
        self.topo = 40
        self.esquerda = 0
        self.largura = 10000
        self.altura = 8000
        self.titulo = "Adicione aqui os dados do funcionário"
        self.CarregarJanela()
    
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()