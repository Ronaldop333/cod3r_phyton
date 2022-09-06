# criando uma classe Data ----------------------------
from random import normalvariate


class Data:
    pass

d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(f'{d1.dia}/{d1.mes}/{d1.ano}')

d2 = Data()
d2.dia = 10
print(f'{d2.dia}')

# Inserindo uma função na classe----------------------------------------------------

class Data:  # criação da classe Data
    def to_str(self): # define uma função para classe "to_str()"
        return f'{self.dia}/{self.mes}/{self.ano}' # self é o valor atribuido a cada atributo da classe

d1 = Data()  # criação do objeto d1
d1.dia = 5  # atribuição de um valor ao atributo dia ( o self procura pelo mesmo atirbuto do objeto com o mesmo criado anteriormente na classe)
d1.mes = 12
d1.ano = 2019
print(d1.to_str()) # uso do ponto para atribuir uma funcionalidade ao objeto

# --generalizando uma função para converter para string--------------------------------------------------

class Data:  # criação da classe Data
    def __str__(self): # utilizando __str__  com ofunção para converte para string
        return f'{self.dia}/{self.mes}/{self.ano}' # self é o valor atribuido a cada atributo da classe

d1 = Data()  # criação do objeto d1
d1.dia = 5  # atribuição de um valor ao atributo dia ( o self procura pelo mesmo atirbuto do objeto com o mesmo criado anteriormente na classe)
d1.mes = 12
d1.ano = 2019
print(d1) # uso do ponto para atribuir uma funcionalidade ao objeto (apenas colocando o nome do objeto)

# --Criando um método construtor--------------------------------------------------
#-- Um método ou função sempre vem com ()-----------------------------------------


class Data: # criando a classe Data 
    # O construtor faz a ligação entre a classe e o objeto gerado
    
    def __init__(self, dia, mes, ano): # construtor com os atributos dia, mes e ano
        self.dia = dia # criando um atributo dia dentro do meu objeto atual e passando o parâmetro dia para o atibuto dia
        self.mes = mes
        self.ano = ano
        
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}' # self é o valor atribuido a cada atributo da classe
        
d1 = Data(6, 2, 2020) # o __init__ requer 3 argumentos
print(d1)

# criando a classe Data ... passando parâmetros no próprio constutor ---------------------------------------------------
class Data: 
    # O construtor faz a ligação entre a classe e o objeto gerado
    
    def __init__(self, dia =4, mes = 8, ano  = 2020): # construtor com os atributos dia, mes e ano
        self.dia = dia # criando um atributo dia dentro do meu objeto atual e passando o parâmetro dia para o atibuto dia
        self.mes = mes
        self.ano = ano
        
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}' # self é o valor atribuido a cada atributo da classe
        
d1 = Data() # atribuindo argumento no construtor
print(d1)

#---Desafio -----------------------------------------------------------------------------------------------------


class Carro: # criando a classe carro
    def __int__(self,velocidade_maxima): # criando o construtor com o parâmetro velocidade máxima
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
    
    c1 = Carro(180)   # definindo a velocidade_máxima de 180
    
    for _ in range(25):
        print(c1.acelerar(8))
        
    for _ in range(10):
        print(c1.frear(delta=20))       
##---------------------------------------------     
    