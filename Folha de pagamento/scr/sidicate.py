from .employee import Employee
from random import randrange

#lguns empregados pertencem ao sindicato (para simplificar, só há um possível sindicato).  O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre  empregados. A taxa sindical é deduzida do salário. Além do mais, o sindicato pode  ocasionalmente cobrar taxas de serviços adicionais a um empregado. Tais taxas de serviço  são submetidas pelo sindicato mensalmente e devem ser deduzidas do próximo  contracheque do empregado. A identificação do empregado no sindicato não é a mesma da  identificação no sistema de folha de pagamento.


class Sindicate():
    def __init__(self, id, taxa_sindical, nome, tipo):
        self.taxa_sincial = taxa_sindical
        self.id = id
        self.nome = nome
        self.tipo = tipo
    

    def __str__(self):
        return(" | "+ self.id +" | " + self.nome + " | " + self.tipo +" | R$" +self.taxa_sincial + " | " )
    
    def get_id(self):
        return self.id
    
    def get_taxa_sindical(self):
        return self.taxa_sincial
    def set_taxa_sindical(self):
        novaTaxa = input("Insira aqui a nova taxa sindical %: \n")
        self.taxa_sincial = novaTaxa
    
    def extra_taxa(self):
        novaTaxa = int(input("Insira aqui a nova taxa sindical %: \n"))
        return novaTaxa

        