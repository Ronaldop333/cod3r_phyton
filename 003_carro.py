class Carro:  # criando a classe carro

    # construtor o objeto tem um único parâmetro que é a velocidade_máxima
    def __init__(self, velocidade_maxima):
        # o parâmetro velociade_maxima recebe ao valor da variável velocidade_maxima
        self.velocidade_maxima = velocidade_maxima 
        #self.velocidade_atual = 0  # definindo velocidade atual

    def __str__(self):  # criação de uma função dentro de uma classe - sempre começa com self
        return f' {self.velocidade_maxima}'


    
c1 = Carro(270)


print(c1)  # chamando a função to_str
