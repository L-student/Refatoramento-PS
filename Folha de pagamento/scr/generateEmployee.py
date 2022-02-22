from .employee import Employee
from .hourly import Hourly
from .commissioned import Commissioned
from .salaried import Salaried

class generateEployee():
    def generate(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day):
        type =  { 
            1 : horista(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day),
            2 : assalariado(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day),
            3 : comissionado(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day)}


def horista(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day):
    hourDay = int(input("Insira quanto o empregado recebe por hora: R$\n"))
    newEmployee = Hourly(name, address, "Horista", 1, MethodPayment, IsSyndicacte, day_in1,day_in2,pay_day, hourDay)
    return Employee
    
def assalariado(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day):
    fixedSalary = input("Insira o salário fixo mensal: R$\n")
    newEmployee = Salaried(name, address, "Assalariado", 2, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day, fixedSalary)   
    return Employee
    
def comissionado(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day):
    fixedSalary = input("Insira o salário fixo mensal: R$\n")
    commissionPercent = float(input("Insira o percentual de comissão % : \n"))
    newEmployee = Commissioned(name, address, "Comissionado", 3, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day, fixedSalary, commissionPercent)
    return Employee









class list_of_employees(Employee):
    def __ini__(self,list):
        super().__init__()
        self.list = []
    
    def __str__(self):
        i = 0
        while(i < len(self.list)):
            return(self.list[i])
            i = i + 1
