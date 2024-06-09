####################################################
# MC102 - Algoritmos e Programação de Computadores #
# Laboratório 15 - Caça-Palavras                   #
# Nome: Marcos Luan Moraes de Oliveira             #
# RA: 221532                                       #
####################################################
### 666 ###

def def_entradas ():

    tabela = []
    entrada = input ()

    while entrada != "0":
        tabela.append (list (entrada))
        entrada = input ()

    lis_palavras = []

    entrada = input ()

    while entrada != "0":
        lis_palavras.append (entrada)
        entrada = input ()

    return tabela, lis_palavras


def def_dicionario (lis_palavras):

    dic_palavras = {}

    for palavra in lis_palavras:

        dic_palavras[palavra] = False

    return dic_palavras

def def_caca_palavra (tabela, palavra, posicao_i, posicao_j, posicao_letra):

    if posicao_letra < len (palavra) - 1: # Não estamos na ultima letra

        if posicao_letra == 0: # Estamos na primeira letra

            for lin in range (len (tabela)):

                for col in range (len (tabela[0])):

                    letra_tabela = tabela[lin][col]

                    if letra_tabela == palavra[0]:
                        posicao_i = lin
                        posicao_j = col

                        if def_caca_palavra (tabela, palavra, posicao_i, posicao_j, posicao_letra + 1):
                            return True
                            

            return False # Significa que não encontrou a primeira letra em toda a tabela

        else: # Não estamos na priemira letra

            for lin in range (len (tabela)):
                letra_tabela = tabela[lin][posicao_j]

                if letra_tabela == palavra[posicao_letra]:
                    posicao_i = lin
                    if def_caca_palavra (tabela, palavra, posicao_i, posicao_j, posicao_letra + 1):
                        return True

            for col in range (len (tabela[0])):
                letra_tabela = tabela[posicao_i][col]

                if letra_tabela == palavra[posicao_letra]:
                    posicao_j = col
                    if def_caca_palavra (tabela, palavra, posicao_i, posicao_j, posicao_letra + 1):
                        return True
            
            return False
        
    else: # Estamos na ultima letra

        for lin in range (len (tabela)):
            letra_tabela = tabela[lin][posicao_j]

            if letra_tabela == palavra[-1]:
                return True

        for col in range (len (tabela[0])):
            letra_tabela = tabela[posicao_i][col]

            if letra_tabela == palavra[-1]:
                return True

        return False
            
            
        
                        




    


def main ():
    
    tabela, lis_palavras = def_entradas ()

    dic_palavra = def_dicionario (lis_palavras) # Dicionario com as palavras e se foram ou não encontradas
    
    

    for palavra in lis_palavras: # Percorre palavra por palavra da lista de palavras dada
        # tabela = def_reset (tabela)
        posicao_i = 0
        posicao_j = 0
        posicao_letra = 0

        
        if def_caca_palavra (tabela, palavra, posicao_i, posicao_j, posicao_letra):
            dic_palavra[palavra] = True
        


    for palavra in dic_palavra:

        if dic_palavra[palavra] == True:
            print ("Palavra", palavra + ": encontrada" )

        else:
            print ("Palavra", palavra +": nao encontrada")








    
main ()
"""
Dada uma matriz, a posição (x,y) e uma sequência
de caracteres, verifica se é possível encontrar 
a palavra

def caca_palavras(m, posX, posY, seq):
#   ...

"""


### 666 ###