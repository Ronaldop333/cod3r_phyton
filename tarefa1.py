
from datetime import datetime

      
        




# criação da classe Tarefa -------------------------------------------------------------------------------------
class Tarefa:  
    def __init__(self, descricao):  # construtor com o atributo descrição
        self.descricao = descricao  # outros atributos self.descrição recebe descrição
        self.feito = False
        self.criacao = datetime.now()  # datetime é função que retorna a data atual


# criação da funcão concluir------------------------------------------------------------------------------------
    def concluir(self):  
        self.feito = True  # se  a tarefa foi concluída o feito recebe True


# Função para passar o resultado para string--------------------------------------------------------------------
    def __str__(self):  # passa as variaveis para string ,,,, com o resultado do algoritmo
        # retorna a descrição da tarefa concluída
        return self.descricao + ('(conlcuida)' if self.feito else' ')



# criação da função principal com a criação de ua lista casa onde são passados os objetos-----------------------
def main():  
    casa = []  # criação de uma lista casa
    casa.append(Tarefa('Passar roupa'))  # adicionando objetos na lista
    casa.append(Tarefa('Lavar prato'))  # adicionando objetos na lista

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f' - {tarefa}')


# informando qual a função principal--------------------------------------------------------------------------
if __name__ == '__main__':
    main()
