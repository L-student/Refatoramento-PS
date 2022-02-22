from .employee import Employee
from .use import*
from datetime import*
from dateutil.relativedelta import relativedelta


class Salaried(Employee):
    def __init__(self, name, adress, type, id,  MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day, Salary_M):
        super().__init__(name, adress, type, id, MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day)
        self.Salary_M = float(Salary_M)
    
    def get_salary(self):
        return self.Salary_M

    
#recebe a cada mês
        
