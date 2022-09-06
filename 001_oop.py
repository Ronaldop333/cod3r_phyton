class Championship:  # criação da classe
    # pass  # bloco vazio associado a classe
    def __str__ (self):  # criação de uma função dentro de uma classe - sempre começa com self
        return f' {self.ano} - {self.team} - {self.games} - {self.country}'


c1 = Championship()  # c1 recebe a classe
c1.ano = 2022  # atributos da classe
c1.team = 20
c1.games = 380
c1.country = 20

print(c1) # chamando a função to_str

