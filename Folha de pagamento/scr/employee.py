
#turtle 
#importante lembrar que o tipo de salário está associado ao tipo de empregado
from datetime import*
from dateutil.relativedelta import relativedelta
from .use import*

class Employee():

    def __init__(self, name, adress, type, id, MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day):
        self.name = name
        self.adress = adress
        self.type = type
        self.id = id
        self.MethodPayment = MethodPayment
        self.IsSyndicacte = IsSyndicacte
        self.day_in1 = day_in1
        self.day_in2 = day_in2
        self.pay_day = pay_day
    
    def __str__(self):
        return( " | "+ self.id +" | " + self.name +" | " + self.type +" | " +self.adress + " | "+ self.IsSyndicacte + " | " )

    def set_name(self):
        newName = input("Insira o novo nome do empregado no sistema:\n")
        self.name = newName
    def get_name(self):
        return self.name

    def set_adress(self):
        newAdress = input("Insira o novo endereço do empregado no sistema: \n")
        self.adress = newAdress
    def get_adress(self):
        return self.adress

    def set_type(self): #criar aqui uma pasta externa com os três tipos associados á números para serem salvos no sistema
        newType = input("Insira o novo tipo de empregado:\n(1) Horista\n(2) Assalariado\n(3) Comissionado")
        return newType
    def get_type(self):
        return self.type      

    def get_id(self):
        return self.id   
    
    def set_MethodPayment(self):#realizar aqui o mesmo menu de tipo de empregadp
            newMethodPayment = input("Insira o novo método de pagamento do empregado:\n(1)Cheque pelos correios\n(2)Cheque em mãos\n(3)Depósito em conta bancária\n")
            self.MethodPayment = newMethodPayment
    def get_MethodPayment(self):
        return self.MethodPayment
    
    def set_IsSyndicacte(self, newIsSyndicacte):
        self.IsSyndicacte = newIsSyndicacte
    def get_IsSyndicacte(self):
        return self.IsSyndicacte
    

    def salary_day(self):
        if(self.pay_day == 1 ):
            day = arrumar_data.dia_semana(self.day_in1,self.day_in2)
            day_today = date.today()
            if(day.weekday() + timedelta(weeks = 1) == day_today.day ):
                return self.Salary_M
            else:
                return 0
        elif(self.pay_day == 2):
            day = arrumar_data.dia_semana(self.day_in1,self.day_in2)
            day_today = date.today()
            if(day.weekday() + timedelta(weeks = 2) == day_today.day ):
                return self.Salary_M
            else:
                return 0
        elif(self.pay_day == 3):
            day_today = date.today()
            if(self.day_in1 +  relativedelta(day=31) == day_today):
                return self.Salary_M
            else:
                return 0
        else:
            print("ok")
    
    def get_agenda(self):
        return self.pay_day
    
    def set_agenda(self, novaAgenda):
        self.pay_day = novaAgenda
    
    def set_pay_day(self,newPayday):
        self.pay_day = newPayday
    
    def salary_day(self):
        if(self.pay_day == 1 ):
            day = arrumar_data.dia_semana(self.day_in1,self.day_in2)
            day_today = date.today()
            if(day + timedelta(weeks = 1) == day_today ):
                return self.Salary_M
            else:
                return 0
        elif(self.pay_day == 2):
            day = arrumar_data.dia_semana(self.day_in1,self.day_in2)
            day_today = date.today()
            if(day + timedelta(weeks = 2) == day_today ):
                return self.Salary_M
            else:
                return 0
        elif(self.pay_day == 3):
            day_today = date.today()
            if(self.day_in1 +  relativedelta(day=31) == day_today):
                return self.Salary_M
            else:
                return 0
        else:
            print("ok")
            
    def get_time1(self):
        return self.day_in1

    def get_time2(self):
        return self.day_in2

    def extra_taxa(self):
        novaTaxa = float(input("Insira aqui a nova taxa sindical %: \n"))
        return novaTaxa
    
    

