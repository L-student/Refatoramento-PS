
from PyQt5 import uic, QtWidgets

def file_function():
    filename = QtWidgets.QFileDialog.getOpenFileName()[0]
    asb.lineEdit.setText(filename)


def path_function():
    filepath = QtWidgets.QFileDialog.getExistingDirectory()
    asb.lineEdit_5.setText(filepath)


def runfs():
    filename = asb.lineEdit.text()
    planilha_fs = asb.lineEdit_4.text()
    planilha_slide = asb.lineEdit_3.text()
    filepath = asb.lineEdit_5.text()
    planilha_leituras = asb.lineEdit_2.text()
    fs_calculated(filename, planilha_fs, planilha_slide, filepath, planilha_leituras)


def runemail():
    filename = asb.lineEdit.text() 
    planilhafs = asb.lineEdit_4.text()
    planilharisco = asb.lineEdit_6.text() 
    planilhacao = asb.lineEdit_7.text()
    send_email(filename, planilhafs, planilharisco, planilhacao)

app = QtWidgets.QApplication([])
asb = uic.loadUi(r'C:\Users\pedro\OneDrive\Área de Trabalho\HidroBR\Geotecnia\Interface.ui')

# Pesquisar arquivo excel
asb.pushButton_3.clicked.connect(file_function)

# Pesquisar caminho das seções
asb.pushButton_7.clicked.connect(path_function)

# Rodar código
asb.pushButton.clicked.connect(runfs)
asb.pushButton_2.clicked.connect(runemail)

# Rodar interface
asb.show()
app.exec()


from PyQt5 import uic, QtWidgets

def main_function():
    janela.label.setText('Você apertou o botão')


app = QtWidgets.QApplication([])
janela = uic.loadUi(r'C:\Users\pedro\OneDrive\Área de Trabalho\teste.ui')

janela.pushButton.clicked.connect(main_function)

janela.show()
app.exec()