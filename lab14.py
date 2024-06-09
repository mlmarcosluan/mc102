######################################################
# MC102 - Algoritmos e Programação de Computadores   #
# Laboratório 14 - Caminho Binário Alternado         #
# Nome: Marcos Luan Moraes de Oliveira               #
# RA: 221532                                         #
######################################################



### 666 ###

def def_entradas ():
    linhas_t = int (input ())

    ### Criação do tabuleiro
    tabuleiro = []
    for i in range (linhas_t):
        linha = [int (x) for x in input ().split ()]
        tabuleiro.append (linha)

    linha_i, coluna_i, linha_f, coluna_f = [int(i) for i in input().split()]
   

    
    return tabuleiro, linha_i, coluna_i, linha_f, coluna_f

def def_caminhos_possiveis (tabuleiro, linha_atual, coluna_atual):

    cor_atual = tabuleiro[linha_atual][coluna_atual]

    caminho_possiveis = []
    if linha_atual > 0: # Podemos ir para o Norte
        proxima_cor = tabuleiro[linha_atual - 1][coluna_atual]

        if cor_atual != proxima_cor and proxima_cor != "X": 
            caminho_possiveis.append ("N")

    if linha_atual < (len (tabuleiro) - 1): # Podemos ir para o Sul
        proxima_cor = tabuleiro[linha_atual + 1][coluna_atual]

        if cor_atual != proxima_cor and proxima_cor != "X":
            caminho_possiveis.append ("S")
    
    if coluna_atual > 0: # Podemos ir para Oeste
        proxima_cor = tabuleiro[linha_atual][coluna_atual - 1]

        if cor_atual != proxima_cor and proxima_cor != "X":
            caminho_possiveis.append ("O")

    if coluna_atual < (len (tabuleiro[0]) - 1): # Podemos ir para Leste
        proxima_cor = tabuleiro[linha_atual][coluna_atual + 1]

        if cor_atual != proxima_cor and proxima_cor != "X":
            caminho_possiveis.append ("L")

    return caminho_possiveis

def def_caminho (tabuleiro, linha_i, coluna_i, linha_f, coluna_f):

    linha_atual = linha_i
    coluna_atual = coluna_i

    if linha_atual == linha_f and coluna_atual == coluna_f: # Ja chegamos no final
        return True

    caminhos_possiveis = def_caminhos_possiveis (tabuleiro, linha_atual, coluna_atual)

    
    for c in caminhos_possiveis:

        if c == "N": # Vamos para o Norte
            cor_atual = tabuleiro[linha_atual][coluna_atual]
            tabuleiro[linha_atual][coluna_atual] = "X"

            if def_caminho (tabuleiro, linha_i - 1, coluna_i, linha_f, coluna_f):
                return True
            else:
                tabuleiro[linha_atual][coluna_atual] = cor_atual

        if c == "S": # Vamos para o Sul
            cor_atual = tabuleiro[linha_atual][coluna_atual]
            tabuleiro[linha_atual][coluna_atual] = "X"

            if def_caminho (tabuleiro, linha_i + 1, coluna_i, linha_f, coluna_f):
                return True
            else:
                tabuleiro[linha_atual][coluna_atual] = cor_atual

        if c == "O": # Vamos para o Oeste
            cor_atual = tabuleiro[linha_atual][coluna_atual]
            tabuleiro[linha_atual][coluna_atual] = "X"

            if def_caminho (tabuleiro, linha_i, coluna_i - 1, linha_f, coluna_f):
                return True
            else:
                tabuleiro[linha_atual][coluna_atual] = cor_atual

        if c == "L": # Vamos para Leste
            cor_atual = tabuleiro[linha_atual][coluna_atual]
            tabuleiro[linha_atual][coluna_atual] = "X"

            if def_caminho (tabuleiro, linha_i, coluna_i + 1, linha_f, coluna_f):
                return True
            else:
                tabuleiro[linha_atual][coluna_atual] = cor_atual

    

    return False


    





def main ():

    tabuleiro, linha_i, coluna_i, linha_f, coluna_f = def_entradas ()

    caminho = def_caminho (tabuleiro, linha_i, coluna_i, linha_f, coluna_f)



    if caminho == True:
        print ("caminho encontrado")

    else:
        print ("caminho nao encontrado")


main ()



### 666 ###