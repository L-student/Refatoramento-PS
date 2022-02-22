from PyQt5 import uic,QtWidgets

def funcao_principal():
    print("hello wolrd")


a = QtWidgets.QApplication([])
selecao = uic.loadUi("Folha_principal.ui")
selecao.pushButton.clicked.connect(funcao_principal)

selecao.show()
a.exe()