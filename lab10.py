######################################################
# MC102 - Algoritmos e Programação de Computadores   #
# Laboratório 10 - Caça ao Tesouro                   #
# Nome: Marcos Luan Moraes de Oliveira               #
# RA: 221532                                         #
######################################################



### 666 ###



def def_movimento (matriz, movimentacao):

    linha = 0
    coluna = 0

    tesouros = 0

    localizacao_atual = matriz[linha][coluna]

    if localizacao_atual == "*": # Caso tenha um tesouro logo na entrada
        tesouros += 1
        matriz[linha][coluna] = "."

    for mov in movimentacao: # O for ira percorrer cada letra da str de movimentação

        if mov == "N": # Caso o movimento seja para o Norte
            linha -= 1
            localizacao_atual = matriz[linha][coluna]

        elif mov == "S": # Caso o movimento seja para o Sul
            linha += 1
            localizacao_atual = matriz[linha][coluna] 

        elif mov == "L": # Caso o movimento seja para Leste
            coluna += 1
            localizacao_atual = matriz[linha][coluna]
        
        elif mov == "O": # Caso o movimento seja para Oeste
            coluna -= 1
            localizacao_atual = matriz[linha][coluna]

        if localizacao_atual == "*": # Caso tenha um teseouro na localizaçao atual
            tesouros += 1
            matriz[linha][coluna] = "."

    return tesouros, matriz
            


def main ():

    n = int(input())
    matriz = [input().split() for _ in range(n)]

    primeiro_time = input ()

    if primeiro_time == "vermelho": # Caso o primeiro time seja o vermelho
        segundo_time = "azul"
    
    else: # Caso o primeiro time seja o azul
        segundo_time = "vermelho"

    

    tabela_tesouros = {primeiro_time: 0, segundo_time: 0}


    numero_jogadores = int (input ())

    for i in range (numero_jogadores):
        movimentacao = input ()

        tesouros_encontrados, matriz = def_movimento (matriz, movimentacao)

        if i % 2 == 0: # É a vez do primeiro time

            tabela_tesouros[primeiro_time] += tesouros_encontrados

        else: # É a vez do segundo time

            tabela_tesouros[segundo_time] += tesouros_encontrados

        
    tesouros_azul = tabela_tesouros["azul"]
    tesouros_vermelho = tabela_tesouros["vermelho"]

    if tesouros_azul > tesouros_vermelho: # O time azul ganhou
        ganhador = "Vitoria do time azul"

    elif tesouros_azul < tesouros_vermelho: # O time vermelho ganhou
        ganhador = "Vitoria do time vermelho"

    else: # Deu empate
        ganhador = "Empate"

    print ("Tesouros encontrados pelo time azul:", tesouros_azul)
    print ("Tesouros encontrados pelo time vermelho:", tesouros_vermelho)
    print (ganhador)

main ()

"""
# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]

# Leitura e processamento dos caminhos



# Impressão da saída
"""


### 666 ###