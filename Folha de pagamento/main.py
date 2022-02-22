from tkinter import Wm
from scr.employee import*
from scr.commissioned import Commissioned
from scr.generateEmployee import generateEployee
from scr.salaried import Salaried
from scr.hourly import Hourly
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 
import random
from scr.sidicate import Sindicate
from datetime import*
import time


def main():
    print("\nFolha de pagamento.\n")
    print("Seja bem vindo/a!!\nPor favo, selecione a opção desejada: \n\n")
    print("1) Adição de um empregado;\n2) Mostrar lista de empregados\n3) Alterar detalhes de um empregado;\n4) Lançar um Cartão de Ponto; \n5) Lançar um Resultado Venda;\n6) Lançar uma taxa de serviço;\n7) Rodar a folha de pagamento para hoje;\n8) Undo/redo;\n9) Agenda de Pagamento;\n10) Criação de Novas Agendas de Pagamento;\n11) Mostrar lista de empregados do sindicato\n12) Remoção de um empregado; \n13) Sair\n")
    number = int(input(""))
    num = 0
    numR = 0
    numS = 0
    number_actions = 0
    numero_agenda = 4
    empregados = []
    sindicato = []
    actions = []
    salarios = []
    dia_hoje = date.today()
    while(True):
        actions.insert(number_actions,number)
        if(number == 1):#def __init__(self, name, adress, type, id, salary, MethodPayment,IsSidcate):
            name = input("Insira o nome do empregado:\n")
            address = input("Insira aqui o endereço do empregado:\n")
            type = int(input("Insira aqui o tipo do empregado:\n(1) Horista\n(2) Assalariado\n(3) Comissionado\n"))
            MethodPayment = int(input("Insira aqui o método de pagamento escolhido pelo empregado:\n(1)Cheque pelos correios\n(2)Cheque em mãos\n(3)Depósito em conta bancária\n"))
            IsSyndicacte = input("O novo empregado pertence ao sindicato? (s \ n)\n")
            isd = 0
            while(isd == 0):
                if(IsSyndicacte == "s"):
                    isd = 1
                    taxa_sindical = input("Informe a taxa do sindicato: R$\n")
                    tipo = "!"
                    if (type == 1):
                        tipo = "Horista"
                    elif (type == 2):
                        tipo = "Assalariado"
                    elif (type == 3):
                        tipo = "Comissionado"
                    num3 = str(numS)
                    newSyndcate = Sindicate(num3,taxa_sindical,name,tipo)
                    sindicato.insert(numS, newSyndcate)
                    numS = numS + 1
                    IsSyndicacte = "Sim"
                    print("Empregado adicionado do sindicato com sucesso!\n")
                    
                elif(IsSyndicacte == "n"):
                    IsSyndicacte = "Não"
                    isd = 1
                    
                else:
                    print("Opçaõ inválida")
                    IsSyndicacte = input("O novo empregado pertence ao sindicato? (s \ n)\n")
                day_in1 = datetime.today()
                day_in2 = day_in1.weekday()
                newEmployee = generateEployee.generate(type,name,address, num ,MethodPayment,IsSyndicacte,day_in1,day_in2,0)
                empregados.insert(num, newEmployee)
            
            print("Novo funcionário adicionado com sucesso!")
            salarios.insert(num,0)
            num = num + 1
            numR = numR + 1
            
            

        elif(number == 12):
            #remover um empregado
            print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
            rand = 0 
            while(rand != numR  ):
                print(empregados[rand])
                rand = rand + 1
            
            id = int(input("Insira o id do empregado que deseja retirar do sistema: \n"))
            salarios.pop(id)
            empregados.pop(id)
            print("Funcionário removido com sucesso!")
            numR = numR - 1

        elif(number == 3):
            #Alterar detalhes de um empregado
            change = int(input("O que deseja alternar no empregado?\n(1)Nome\n(2)Tipo\n(3)Endereço\n(4)Status no sindicato\n"))
            if(change == 1):
                #muda o nome
                print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
                rand = 0 
                while(rand != numR):
                    print(empregados[rand])
                    rand = rand + 1
                id = int(input("Insira o id do empregado que deseja alterar o nome: \n"))
                new = empregados[id]
                empregados.pop(id)
                new.set_name()
                empregados.insert(id, new)
                print("Operação realizada com sucesso!\n")
            
            elif(change == 2):
                #muda o tipo 
                print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
                rand = 0 
                while(rand != numR  ):
                    print(empregados[rand])
                    rand = rand + 1
                id = int(input("Insira o id do empregado que deseja alterar o tipo: \n"))
                newType = int(input("Insira o novo tipo de empregado:\n(1) Horista\n(2) Assalariado\n(3) Comissionado\n"))
                newEmployee = empregados[id]
                empregados.pop(id)
                print(newEmployee.get_name())
                newEmployee = generateEployee.generate(newType,newEmployee.get_name(),newEmployee.get_adress(),newEmployee.get_id(),newEmployee.get_MethodPayment(),newEmployee.get_IsSyndicacte(),newEmployee.get_time1(), newEmployee.get_time2(), newEmployee.get_agenda())
                empregados.insert(id, newEmployee)
                print("Operação realizada com sucesso!\n")
            
            elif(change == 3):
                #Muda o endereço
                print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
                rand = 0 
                while(rand != numR  ):
                    print(empregados[rand])
                    rand = rand + 1
                id = int(input("Insira o id do empregado que deseja alterar o enderço: \n"))
                new = empregados[id]
                empregados.pop(id)
                new.set_adress()
                empregados.insert(id, new)
                print("Operação realizada com sucesso!\n")
            
            elif(change == 4):
                #Altera se é do sindicato ou não e detalhes do sindicato
                print("\n | ID|  Nome  | Tipo | Taxa sindical |")
                rand1 = 0
                while(rand1 != numS  ):
                    print(sindicato[rand1])
                    rand1 = rand1 + 1
                print("\n")
                make = int(input("Selecione o que deseja fazer com o status do empregado no sindicato:\n(1) Remover \n(2) Adicionar um funcionário ao sindicato \n(3) Altear a taxa sindical \n"))
                if(make == 1):
                    var = int(input("Insira o ID do empregado que deseja excluir do sindicato: \n"))
                    print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
                    rand = 0 
                    while(rand != numR  ):
                        print(empregados[rand])
                        rand = rand + 1
                    id = int(input("Insira o id do empregado (correspondente a cima) que deseja alterar o status no sindicato: \n"))
                    sindicato.pop(var)
                    IsSyndicacte = "Não"
                    numS = numS - 1
                    empregados[id].set_IsSyndicacte(IsSyndicacte)
                    print("Empregado removido do sindicato com sucesso!\n")
                
                elif(make == 2):
                    print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
                    rand = 0 
                    while(rand != numR  ):
                        print(empregados[rand])
                        rand = rand + 1
                    id = int(input("Insira o id do empregado (correspondente a cima) que deseja alterar o status no sindicato: \n"))
                    tipo = empregados[id].get_type()
                    name1 = empregados[id].get_name()
                    num3 = str(numS)
                    txs = input("Insira a taxa do sindicato: \n")
                    newSyndcate = Sindicate(num3,txs,name1,tipo)
                    sindicato.insert(numS, newSyndcate)
                    numS = numS + 1
                    IsSyndicacte = "Sim"
                    empregados[id].set_IsSyndicacte(IsSyndicacte)
                    print("Empregado adicionado do sindicato com sucesso!\n")
                
                elif(make == 3):
                    var = int(input("Insira o ID do empregado que deseja alterar a taxa do sindicato: \n"))
                    sindicato[var].set_taxa_sindical()
                    print("Operação realizada com sucesso!\n")
                
                else: 
                    print("Entrada inválida\n")
            
            else:
                print("Entrada inválida\n")

        elif(number == 4):
            #lançar cartão de ponto
            print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
            rand2 = 0
            while(rand2 != numR  ):
                print(empregados[rand2])
                rand2 = rand2 + 1
            print("\n")
            id = int(input("Insira o id do horista que deseja lançar um cartão de ponto: \n"))
            entrada_H = int(input("Insira a hora de entrada (0 - 24): "))
            entrada_M = int(input("Insira os minutos da hora de entrada (0 - 60): "))
            saida_H = int(input("Insira a hora de saída(0 - 24):"))
            saida_M = int(input("Insira os minutos da hora de saida (0 - 60): "))
            entrada = entrada_H + (entrada_M/60)
            saida = saida_H + (saida_M/60)
            salario = salarios[id] + empregados[id].day(entrada,saida)
            salarios.insert(id,salario)
            print("Operação realizada com sucesso!\n")
        
        elif(number == 5):
            #Lançar um Resultado Venda
            print("\n | ID|  Nome    | Tipo | Endereço | No sindicato |")
            rand3 = 0
            while(rand3 != numR  ):
                print(empregados[rand3])
                rand3 = rand3 + 1
            print("\n")
            id = int(input("Insira o id do empregado comissionado que deseja lançar um resultado de venda: \n"))
            dia = int(input("Insira aqui o dia da venda: \n"))
            mes = int(input("Insira aqui o mês da venda: \n"))
            valor = int(input("Insira aqui o valor da venda: \n"))
            comissao = salarios[id] + empregados[id].set_commssion_day(valor)
            salarios.insert(id, comissao)
            print("Operação realizada com sucesso!\n")
        
        elif(number == 6):
            #Lançar uma taxa de serviço;
            print("\n | ID|  Nome  | Tipo | Taxa sindical |")
            rand4 = 0
            while(rand4 != numS  ):
                print(sindicato[rand4])
                rand4 = rand4 + 1
            print("\n")
            id = int(input("Insira o id do empregado do sindicato que deseja lançar uma taxa de serviço: \n"))
            taxaNova = sindicato[id].extra_taxa()
            txn = salarios[id] + taxaNova
            salarios.insert(id, txn)
            print("Operação realizada com sucesso!\n")
        
        elif(number == 7):
            #Rodar a folha de pagamento para hoje
            rand12 = 0
            p = 0
            salario = 0
            while(rand12 != numR  ):
                if(empregados[rand12].salary_day() != 0):
                    print(empregados[rand12])
                    if(empregados[rand12].type() == "Comissionado"):
                        salario = salarios[rand12] + empregados[rand12].get_Salary_M()
                    elif(empregados[rand12].type() == "Assalariado"):
                        salario = empregados[rand12].get_Salary_M()
                    elif(empregados[rand12].type() == "Horista"):
                        salario = salarios[rand12]
                    print("Salário correspondente: ", salario)
                    p = p +1
                rand12 = rand12 + 1
            if(p == 0):
                print("Nenhum empregado será pago hoje\n")
            else:
                p2 = str(p)
                print(p2 +" empregados foram pagos hoje\n")
        
        elif(number == 8):
            #Undo/redo
            id1 = int(input("Insira se deseja realizar: \n(1)Undo \n(2)Redo: \n"))
            if(id1 == 1):
                print("Deseja desfazer a ação:", actions[number_actions], "(s/n) ?")
                resp = input("")
                if(resp == "s"):
                    number_actions = number_actions - 1
                    print("Operação realizada com sucesso!\n")
                else:
                    print("Operação não realizada.\n")
            elif(id1 == 2):
                print("Deseja desfazer a ação:", actions[number_actions], "(s/n) ?")
                resp = input("")
                if(resp == "s"):
                    actions.insert(actions[number_actions])
                    print("Operação realizada com sucesso!\n")
                else:
                    print("Operação não realizada.\n")
            
        
        elif(number == 9):
            #Agenda de Pagamento
            print("As agendas de pagamento são o perído em que cada funcionário recebe o seu salário\nPorfavor, selecione o ID do funcionário que deseja mudar a agenda de pagamento: \n")
            rand9 = 0
            while(rand9 != numR  ):
                print(empregados[rand9])
                rand9 = rand9 + 1
            id = int(input(""))
            print("Estas são as agendas de pagamento atuais disponíveis:\n")
            agendas = open("agenda.txt", "r")
            payday = agendas.readlines()
            for linha in payday:
                print(linha)
            agendas.close()
            print("O funcionário atualmente está cadastrado no tipo de agenda:", empregados[id].get_agenda())
            mudar = int(input("Porfavor, selecione a nova agenda de pagamento para o(a)  funcionário(a) " + empregados[id].get_name()+ ":\n"))
            empregados[id].set_agenda(mudar)
            print("Operação realizada com sucesso!\n")

        elif(number == 10):
            #Criação de Novas Agendas de Pagamento
            print("As agendas de pagamento são o perído em que cada funcionário recebe o seu salário\n")
            print("Nesta opção é possível adicionar uma nova agenda de pagamento\n")
            print("A seguir será enumerado algun exemplos.\n")
            print( "mensal 1: dia 1 de todo  mês \nmensal 7: dia 7 de todo mês \nmensal $: último  dia útil de todo mês\nsemanal 1 segunda: toda semana  às segundas-feiras\nsemanal 1 sexta: toda semana às  sextas-feiras\nsemanal 2 segunda: a cada 2 semanas às  segundas-feiras ")
            mandar = input(" ")
            numa = str(numero_agenda)
            arquivo = open('agenda.txt', 'r') # Abra o arquivo (leitura)
            conteudo = arquivo.readlines()
            conteudo.append( "\n(" +numa+") "+ mandar)   # insira seu conteúdo
            numero_agenda = numero_agenda + 1

            arquivo = open('agenda.txt', 'w') # Abre novamente o arquivo (escrita)
            arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

            arquivo.close()
            print("Operação realizada com sucesso!\n")
        elif(number == 2):
            print("\n | ID|  Nome    | Tipo | Endereço |No sindicato |")
            rand12 = 0
            while(rand12 != numR  ):
                print(empregados[rand12])
                rand12 = rand12 + 1
            print("\n")
            #mostrar lista de empregados
        elif(number == 11):
            print("\n | ID|  Nome  | Tipo | Taxa sindical |")
            rand1 = 0
            while(rand1 != numS  ):
                print(sindicato[rand1])
                rand1 = rand1 + 1
            print("\n")
        elif(number == 13):
            return
        else:
            print("Entrada inválida")
        
        actions.insert(number_actions,number)
        number_actions = number_actions + 1
        print("\nFolha de pagamento.\n")
        number = int(input("1) Adição de um empregado;\n2) Mostrar lista de empregados\n3) Alterar detalhes de um empregado;\n4) Lançar um Cartão de Ponto; \n5) Lançar um Resultado Venda;\n6) Lançar uma taxa de serviço;\n7) Rodar a folha de pagamento para hoje;\n8) Undo/redo;\n9) Agenda de Pagamento;\n10) Criação de Novas Agendas de Pagamento;\n11) Mostrar lista de empregados do sindicato\n12) Remoção de um empregado; \n13) Sair\n"))
  
main()


