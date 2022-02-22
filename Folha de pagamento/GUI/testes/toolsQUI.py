import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from toolsgui import window2

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

class window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 40
        self.esquerda = 0
        self.largura = 10000
        self.altura = 8000
        self.titulo = "Folha de pagamento"
        #Buttons----------------------------------------------------------------------------------------------------------------------------------------------
        buttonOne = QPushButton('Adição de um empregado', self)
        buttonOne.move(200,300)
        buttonOne.resize(300,100)
        buttonOne.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonTwo = QPushButton('Remoção de um empregado', self)
        buttonTwo.move(600,300)
        buttonTwo.resize(300,100)
        buttonTwo.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonThree = QPushButton('Alterar detalhes de um empregado', self)
        buttonThree.move(1000,300)
        buttonThree.resize(300,100)
        buttonThree.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonFour = QPushButton('Lançar um Cartão de Ponto', self)
        buttonFour.move(1400,300)
        buttonFour.resize(300,100)
        buttonFour.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonFive = QPushButton('Lançar um Resultado Venda', self)
        buttonFive.move(200,500)
        buttonFive.resize(300,100)
        buttonFive.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonSix = QPushButton('Lançar uma taxa de serviço', self)
        buttonSix.move(600,500)
        buttonSix.resize(300,100)
        buttonSix.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonSeven = QPushButton('Rodar a folha de pagamento para hoje', self)
        buttonSeven.move(1000,500)
        buttonSeven.resize(300,100)
        buttonSeven.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonEightUndo = QPushButton('Undo/redo', self)
        buttonEightUndo.move(1400,500)
        buttonEightUndo.resize(150,100)
        buttonEightUndo.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonEightRedo = QPushButton('Undo/redo', self)
        buttonEightRedo.move(1550,500)
        buttonEightRedo.resize(150,100)
        buttonEightRedo.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonNine = QPushButton('Agenda de Pagamento', self)
        buttonNine.move(350,700)
        buttonNine.resize(300,100)
        buttonNine.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonTen = QPushButton('Adicionar empregado', self)
        buttonTen.move(1150,700)
        buttonTen.resize(300,100)
        buttonTen.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        buttonExit = QPushButton('Saída', self)
        buttonExit.move(900,900)
        buttonExit.resize(80,50)
        buttonExit.setStyleSheet('QPushButton{background-color:#126470; font: bold; font-size: 14px}')

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        
        buttonOne.clicked.connect(self.buttonOneClick)
        buttonTwo.clicked.connect(self.buttonTwoClick)
        buttonThree.clicked.connect(self.buttonThreeClick)
        buttonFour.clicked.connect(self.buttonFourClick)
        buttonFive.clicked.connect(self.buttonFiveClick)
        buttonSix.clicked.connect(self.buttonSixClick)
        buttonSeven.clicked.connect(self.buttonSevenClick)
        buttonEightUndo.clicked.connect(self.buttonEightUndoClick)
        buttonEightRedo.clicked.connect(self.buttonEightRedoClick)
        buttonNine.clicked.connect(self.buttonNineClick)
        buttonTen.clicked.connect(self.buttonTenClick)
        buttonExit.clicked.connect(self.buttonExitClick)

        #Lable------------------------------------------------------------------------------------------------------------------------------

        Lable1 = QLabel(self)
        Lable1.setText('Folha de pagamento')
        Lable1.move(850,60)
        Lable1.resize(300,150)
        Lable1.setStyleSheet('QLabel{ font: bold; font-size: 20px}')


        self.CarregarJanela()
    
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    #Fuctions Buttons -------------------------------------------------------------------------------------------------------------------------------------
    def buttonOneClick(self):
        print("this button was clicked")
    
    def buttonTwoClick(self):
        print("this button was clicked")
    
    def buttonThreeClick(self):
        print("this button was clicked")

    def buttonFourClick(self):
        print("this button was clicked")

    def buttonFiveClick(self):
        print("this button was clicked")

    def buttonSixClick(self):
        print("this button was clicked")

    def buttonSevenClick(self):
        print("this button was clicked")

    def buttonEightUndoClick(self):
        print("this button was clicked")

    def buttonEightRedoClick(self):
        print("this button was clicked")
    
    def buttonNineClick(self):
        print("this button was clicked")

    def buttonTenClick(self):
        print("this button was clicked")

    def buttonExitClick(self):
        print("this button was clicked")

aplicacao = QApplication(sys.argv)
j = window1()
sys.exit(aplicacao.exec_())