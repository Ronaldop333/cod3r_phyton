#---Desafio -----------------------------------------------------------------------------------------------------


class Carro: # criando a classe carro
    def __init__(self,velocidade_maxima): # criando o construtor com o parâmetro velocidade máxima
        self.velocidade_maxima = velocidade_maxima  # criando o atributo velocidade máxima
        self.velocidade_atual = 0  # criando o atributo velocidade atual
        
    def acelerar(self, delta = 5): # criação do método acelerar
        maxima = self.velocidade_maxima #criação da variável maxima
        nova = self.velocidade_atual + delta  #criação da variável nova
        self.velocidade_atual = nova if nova <= maxima else maxima # a velocidade atual é igual nova, se a nova é menor ou igual a velocidade nova
        return self.velocidade_atual

        
    
    def frear(self, delta = 5): # criação do método frear
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0 # self velocidade atual recebe a nova se ela for maior que zero
        return self.velocidade_atual
        
          



##---------------------------------------------
if __name__ == '__main__':
    c1 = Carro(180)
    
    
    
    for _ in range(25):
        print(c1.acelerar(8))
        
    for _ in range(10):
        print(c1.frear(delta=20))       
##---------------------------------------------   