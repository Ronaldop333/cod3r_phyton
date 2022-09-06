from __future__ import annotations
from email import message


class Data:

    # construtor
    def __init__(self, dia=1, mes=2, ano=3333):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    # ------------------------------------------

    def __str__(self):
        return f'{self.dia},{self.mes},{self.ano}'


d1 = Data()
d1.dia = 5
# d1.mes = 12
# d1.ano = 1999
print(d1)

print(idade)

d2 = Data(7, 7, 7777)
# d2.dia = 12
# d2.mes = 7
# d2.ano = 2000
print(d2)
