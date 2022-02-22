from .salaried import Salaried
from datetime import*
from dateutil.relativedelta import relativedelta
from .use import*

class Commissioned(Salaried):
    def __init__(self, name, adress, type, id, MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day, Salary_M, commissionP):
        super().__init__(name, adress, type, id,  MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day,Salary_M)
        self.commissionP = float(commissionP)

    def set_commssion_day(self, valor):
        ganho = (valor * self.commissionP/100)
        return ganho
    
    def get_commission(self):
        return self.commissionP
    def put_commission(self):
        nemCommission = float(input('Adicione aqui o novo percentual de comissão do funcionário'))
    
    def input_informations(self,day,money):
        self.day = input("")
        self.money = input("")
    
    def reciveSalary(self):
        newSalary = self.Salary_M /2 + (self.money * self.commissionP)
        return newSalary

#aqui recebe a cada duas semanas


    