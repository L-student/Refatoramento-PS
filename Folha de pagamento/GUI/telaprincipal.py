from PyQt5 import uic,QtWidgets

def Button_one():
    #para uma janela para colher as informações dos funcionários
    linker.frame_add_fun.show()
    print("Clicou botão 1")

def B_O_Box():
    linker.frameSindicatoSn.show()
def B_O_Box2():
    linker.frameSindicatoSn.close()

def B_O_Box3():
    tipo = linker.comboBox.currentText()
    if (tipo == 'Horista'):
        linker.frame_Horista.show()
        linker.frame_Assalariado.close()
        linker.frame_Comissionado.close()
        print(tipo)
    elif (tipo == "Assalariado"):
        linker.frame_Assalariado.show()
        linker.frame_Comissionado.close()
        linker.frame_Horista.close()
        print(tipo)
    elif (tipo == "Comssionado"):
        linker.frame_Horista.close()
        linker.frame_Assalariado.show()
        linker.frame_Comissionado.show()
        print(tipo)
    
def B_O_Box4():
    linker.frame_add_fun.close()
    

def Button_two():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 2")

def Button_three():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 3")

def Button_four():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 4")
    
def Button_five():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 5")

def Button_six():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 6")

def Button_seven():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 7")

def Button_eight():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 8")

def Button_nine():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão 9")

def Button_exit():
    #para uma janela para colher as informações dos funcionários
    app.exit()

def Button_undo():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão undo")

def Button_redo():
    #para uma janela para colher as informações dos funcionários
    print("Clicou botão redo")


app = QtWidgets.QApplication([])

linker = uic.loadUi(r'C:\Users\lilic\OneDrive\Documentos\Códigos\Folha de pagamento\GUI\Folha_principal.ui')

linker.addEmployee.clicked.connect(Button_one)

linker.radioButton.clicked.connect(B_O_Box)
linker.radioButton_2.clicked.connect(B_O_Box2)

linker.exit_2.clicked.connect(B_O_Box4)

linker.exit_3.clicked.connect(B_O_Box3)

linker.exclueEmployee.clicked.connect(Button_two)

linker.changeEmployee.clicked.connect(Button_three)

linker.paymentToday.clicked.connect(Button_four)

linker.cartPoit.clicked.connect(Button_five)

linker.serviceText.clicked.connect(Button_six)

linker.addPayment.clicked.connect(Button_seven)

linker.seal_result.clicked.connect(Button_eight)

linker.organize.clicked.connect(Button_nine)

linker.exit.clicked.connect(Button_exit)

linker.undo.clicked.connect(Button_undo)

linker.redo.clicked.connect(Button_redo)

linker.frame_add_fun.close()
linker.frameSindicatoSn.close()
linker.frame_Comissionado.close()
linker.frame_Assalariado.close()
linker.frame_Horista.close()


linker.show()
app.exec()

