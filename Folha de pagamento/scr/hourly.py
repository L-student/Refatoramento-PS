from .employee import Employee
from datetime import*
from dateutil.relativedelta import relativedelta
from .use import*


class Hourly(Employee):
    horas_trabalhadas = []

    def __init__(self, name, adress, type, id, MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day,hourDay):
        super().__init__(name, adress, type, id, MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day)
        self.hourDay = hourDay
        self.entrada = 0.00
        self.saida = 0.00
    
    def __str__(self):
        return( " | "+ self.id +" | " + self.name +" | " + self.type +" | " +self.adress + " | "+ self.IsSyndicacte + " | " )
        teste = Employee(name, adress, type, id, MethodPayment,IsSyndicacte,hourDay) 


    def day(self,entrada, saida):
        self.entrada = entrada
        self.saida = saida
        horas_dia = (saida - entrada)
        salario_dia = 0
        if(horas_dia > 8):
            salario_dia = (8 * self.hourDay) + ((horas_dia - 8) * self.hourDay * 1.5)
        else:
            salario_dia = horas_dia * self.hourDay
        return salario_dia



    
        
