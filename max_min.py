class Carro:  # criando a classe carro
    
    def __init__(self, velocidade_maxima):  #construtor o objeto tem um único parâmetro que é a velocidade_máxima
        self.velocidade_maxima = velocidade_maxima #o parâmetro velociade_maxima recebe ao valor da variável velocidade_maxima
        self.velocidade_atual = 0 # definindo velocidade atual
        
    def acelerar(self, delta=5): # método acelerar
        maxima = self.velocidade_maxima # a variável maxima recebe a velocidade maxima do objeto
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual
        
    def frear(self, delta=5): # método frear
        nova = self.velocidade_atual - delta
        self.veocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual
    
if __name__ == '__main__':
    c1 = Carro(180)
    
    for _ in range(25):
        print(c1.acelerar(10))
        
    for _ in range(10):
        print(c1.frear(delta=20))
        
        
        
     
        