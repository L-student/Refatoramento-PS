from abc import ABCMeta, abstractstaticmethod
from datetime import*
from dateutil.relativedelta import relativedelta


class IUndoRedo(metaclass=ABCMeta):
    """The Undo Redo interface"""
    @abstractstaticmethod
    def history():
        """the history of the states"""

    @abstractstaticmethod
    def undo():
        """for undoing the hsitory of the states"""

    @abstractstaticmethod
    def redo():
        """for redoing the hsitory of the states"""

class arrumar_data():
    def dia_semana(dia_in, semana_in):
        if(semana_in == 1):
            return dia_in + timedelta(days=3)
        elif(semana_in == 2):
            return dia_in + timedelta(days=2)
        elif(semana_in == 3):
            return dia_in + timedelta(days=1)
        elif(semana_in == 4):
            return dia_in + timedelta(days=6)
        elif(semana_in == 5):
            return dia_in 
        elif(semana_in == 6):
            return dia_in + timedelta(days=5)
        elif(semana_in == 7):
            return dia_in + timedelta(days=4)
