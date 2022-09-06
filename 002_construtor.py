
class Championship:  # criação da classe
    # pass  # bloco vazio associado a classe
    # criação do construtor com os parâmetros ano, team, games, country
    def __init__(self, ano, team, games, country):
        self.ano = ano
        self.team = team
        self.games = games
        self.country = country

    def __str__(self):  # criação de uma função dentro de uma classe - sempre começa com self
        return f' {self.ano} - {self.team} - {self.games} - {self.country}'


c1 = Championship(2022, 20, 380, 20)  # inserindo valores nos parâmetros... aqui o self corresponde c1

print(c1)  # chamando a função to_str
