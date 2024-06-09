####################################################
# MC102 - Algoritmos e Programação de Computadores #
# Laboratório 12 - Redimensionamento de Imagens    #
# Nome: Marcos Luan Moraes de Oliviera             #
# RA: 221532                                       #
####################################################

def def_entradas (): # Função para os inputs

    p2 = input () 
    colunas_img_o, linhas_img_o = [int(x) for x in input().split()]
    valor_max = input () 

    imagem_original = []
    for i in range(linhas_img_o):
        linha = [int(x) for x in input().split()]
        imagem_original.append(linha)

    tipo_de_red = input ()

    return p2, colunas_img_o, linhas_img_o, valor_max, imagem_original, tipo_de_red

def def_imprimir_imagem(imagem): # Função para as saidas

    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i])) 

def def_expande (imagem_original): # Função que cria uma matriz expandida mas com 0s

    linhas_exp = (len (imagem_original) * 2 ) - 1
    colunas_exp = (len (imagem_original[0]) * 2) -1

    imagem_exp = []
    linha = []
    for lin in range (linhas_exp):

        for col in range (colunas_exp):
            linha.append (0)

        imagem_exp.append (linha)
        linha = []

    return imagem_exp

def def_expansao (imagem_original): # Função de expansão da imagem

    
    # Pegamos a imagem original(A) de tamanho A = (n X m) e transformamos em uma imagem B = (2n -1 X 2m -1)

    linhas_o = len (imagem_original)
    colunas_o = len (imagem_original[0])

    # Com isso nossa imagem expandida ficara com tamanho:

    linhas_exp = (linhas_o * 2) - 1
    colunas_exp = (colunas_o * 2) - 1

    # Criando uma imagem expandida mas apenas com 0s

    imagem_exp = def_expande (imagem_original)

    ### Passo 1 ###
    
    for lin in range (linhas_o): # Percorremos pelas linhas da imagem original

        for col in range (colunas_o): # Percorremos pelas colunas da imagem original

            elemento_o = imagem_original[lin][col]

            i = lin + 1
            j = col + 1

            if 1 <= i <= linhas_o and 1 <= j <= colunas_o: # Aqui podemos usar a regra direto
                # O elemento P(i, j) Sera colocado na posição P((i * 2 - 1), (j * 2 - 1))
                # aplicando a regra
                i_r = i * 2 - 1 
                j_r = j * 2 - 1 

                imagem_exp[i_r - 1][j_r - 1] = elemento_o

            else: # Não podemos usar a regra de priemira, logo ou a coluna == 0 ou a linha == 0

                if lin == 0:
                    i_r = 0
                else: # lin != 0
                    i_r = i * 2 -1
                
                if col == 0:
                    j_r = 0
                else:
                    j_r = j * 2 - 1

                imagem_exp[i_r - 1][j_r - 1] = elemento_o

    ### Passo 2 ###

    # Cada P(i, j) da imagem expandida tal que i é impar e j é par, é preenchido pela média de valores
    # P(i, (j - 1)) e P(i, (J + 1))

    for lin in range (linhas_exp):

        for col in range (colunas_exp):

            i = lin + 1
            j = col + 1

            if i % 2 == 0: # i é Par
                i_paridade = "par"
            else: # i é impar
                i_paridade = "impar"

            if j % 2 == 0: # j é par
                j_paridade = "par"
            else: # j é impar
                j_paridade = "impar"

            if i_paridade == "impar" and j_paridade == "par": # Podemos preencher com a média

                elemento_ant = imagem_exp [lin][col - 1]
                elemento_pos = imagem_exp [lin][col + 1]

                media = int ((elemento_ant + elemento_pos) / 2)

                imagem_exp[lin][col] = media 

    
    ### Passo 3 ###

    # Cada P(i, j) da imagem expandida tal que i é par e j é impar, é preenchido pela média de valores
    # P(i - 1, j) e P(i - 1, j)

    for lin in range (linhas_exp):

        for col in range (colunas_exp):

            i = lin + 1
            j = col + 1

            if i % 2 == 0: # i é Par
                i_paridade = "par"
            else: # i é impar
                i_paridade = "impar"

            if j % 2 == 0: # j é par
                j_paridade = "par"
            else: # j é impar
                j_paridade = "impar"

            if i_paridade == "par" and j_paridade == "impar": # Podemos preencher

                elemento_ant = imagem_exp [lin - 1][col]
                elemento_pos = imagem_exp [lin + 1][col]

                media = int ((elemento_ant + elemento_pos) / 2)

                imagem_exp[lin][col] = media 

            
    ### Passo 4 ###

    # Cada P(i, j) da imagem expandida tal que i é par e j é par, é preenchido pela média de valores
    # P(i - 1, j - 1) e P(i - 1, j + 1)

    for lin in range (linhas_exp):

        for col in range (colunas_exp):

            i = lin + 1
            j = col + 1

            if i % 2 == 0: # i é Par
                i_paridade = "par"
            else: # i é impar
                i_paridade = "impar"

            if j % 2 == 0: # j é par
                j_paridade = "par"
            else: # j é impar
                j_paridade = "impar"

            if i_paridade == "par" and j_paridade == "par": # Podemos preencher

                elemento_1 = imagem_exp [lin - 1][col - 1]
                elemento_2 = imagem_exp [lin - 1][col + 1]
                elemento_3 = imagem_exp [lin + 1][col - 1]
                elemento_4 = imagem_exp [lin + 1][col + 1]
                

                media = int ((elemento_1 + elemento_2 + elemento_3 + elemento_4) / 4)

                imagem_exp[lin][col] = media 

    return imagem_exp

def def_calcula_linhas_ret (imagem_original): # Função que calculas as linhas da imagem retraida
    linhas_o = len (imagem_original)
    colunas_o = len (imagem_original[0])

    ### Calculando a paridade da matriz original ###
    if linhas_o % 2 == 0: # Numero de linhas da imagem original é par
        paridade_linhas_o = "par"
    else: # Numero de linhas da imagem original é impar
        paridade_linhas_o = "impar"
    if colunas_o % 2 == 0: # Numero de colunas da imagem original é par
        paridade_colunas_o = "par"
    else: # Numero de colunas da imagem original é impar
        paridade_colunas_o = "impar"
    
    ### Calculando o numero de linhas e colunas da matriz retratada
    if paridade_linhas_o == "par": # Numero de linhas da imagem original é par
        linhas_ret = linhas_o / 2
    else: # Numero de linhas da imagem original é impar
        linhas_ret = (linhas_o + 1) / 2

    if paridade_colunas_o == "par": # Numero de colunas da imagem original é par
        colunas_ret = colunas_o / 2
    else: # Numero de colunas da imagem original é impar
        colunas_ret = (colunas_o + 1) / 2

    if linhas_ret % 2 == 0: # Numero de linhas da imagem retraida é par
        paridades_linha_ret = "par"

    else: # Numero de linhas da imagem retraida é impar
        paridades_linha_ret = "impar"

    if colunas_ret % 2 == 0: # Numero de colunas da imagem retraida é par
        paridade_colunas_ret = "par"
    else: # Numero de colunas da imagem retraida é impar
        paridade_colunas_ret = "impar"


    return int (linhas_ret), int (colunas_ret), paridades_linha_ret, paridade_colunas_ret

def def_imagem_ret (linhas_ret, colunas_ret): # Função que cria uma matriz retraida mas com 0s

    matriz_ret = []
    linha = []

    for lin in range (linhas_ret):

        for col in range (colunas_ret):
            linha.append (0)

        matriz_ret.append (linha)
        linha = []


    return matriz_ret

def def_retracao (imagem_original): # Função retraçao

    linhas_o = len (imagem_original) 
    colunas_o = len (imagem_original[0])

    if linhas_o % 2 == 0: # O numero de linhas da matriz original é par
        paridade_linha_o = "par"
    else: # O numero de linhas da matriz original é impar
        paridade_linha_o = "impar"

    if colunas_o % 2 == 0: # O numero de colunas da matriz original é par
        paridade_coluna_o = "par"
    else: # O numero de colunas da matriz original é impar
        paridade_coluna_o = "impar"

    linhas_ret, colunas_ret, paridade_linha_ret, paridade_coluna_ret = def_calcula_linhas_ret (imagem_original)

    imagem_ret = def_imagem_ret (linhas_ret, colunas_ret) # Matriz composta apenas por 0s



    if paridade_linha_o == "par" and paridade_coluna_o == "par": # Ambos são pares então pode aplicar a regra

        for lin in range (linhas_ret):

            for col in range (colunas_ret):

                soma = (imagem_original[lin * 2][col * 2]) + (imagem_original [(lin * 2) + 1][col * 2]) + (imagem_original[lin * 2][(col * 2 + 1)]) + (imagem_original[(lin * 2) + 1][(col * 2 + 1)])
                media = int (soma / 4)
                imagem_ret [lin][col] = media

    elif paridade_linha_o == "impar" and paridade_coluna_o == "par":

        for lin in range (linhas_ret - 1):

            for col in range (colunas_ret):

                soma = (imagem_original[lin * 2][col * 2]) + (imagem_original [(lin * 2) + 1][(col * 2)]) + (imagem_original[lin * 2][(col * 2) + 1]) + (imagem_original[(lin * 2) + 1][(col * 2) + 1])
                media = int (soma / 4) 
                imagem_ret [lin][col] = media

        # Agora temos que calcular a ultima linha

        for col in range (colunas_ret):

            soma = (imagem_original [-1][col * 2]) + (imagem_original [-1][(col * 2) + 1])
            media = int (soma / 2)
            imagem_ret [-1][col] = media


    elif paridade_linha_o == "par" and paridade_coluna_o == "impar":

        for lin in range (linhas_ret):

            for col in range (colunas_ret - 1):

                soma = (imagem_original[lin * 2][col * 2]) + (imagem_original [(lin * 2) + 1][col * 2]) + (imagem_original[lin * 2][(col * 2 + 1)]) + (imagem_original[(lin * 2) + 1][(col * 2 + 1)])
                media = int (soma / 4)
                imagem_ret [lin][col] = media

        # Agora temos que calcular para as ultimas colunas

        for lin in range (linhas_ret):

            soma = (imagem_original[lin * 2][-1]) + (imagem_original[(lin * 2) + 1][-1])
            media = int (soma / 2)
            imagem_ret[lin][-1] = media

    elif paridade_linha_o == "impar" and paridade_coluna_o == "impar":

        for lin in range (linhas_ret - 1):

            for col in range (colunas_ret - 1):

                soma = (imagem_original[lin * 2][col * 2]) + (imagem_original [(lin * 2) + 1][col * 2]) + (imagem_original[lin * 2][(col * 2 + 1)]) + (imagem_original[(lin * 2) + 1][(col * 2 + 1)])
                media = int (soma / 4)
                imagem_ret [lin][col] = media

        # Agora temos que calcular para a ultima linhas e a ultima coluna
        
        for col in range (colunas_ret - 1):

            soma = (imagem_original [-1][col * 2]) + (imagem_original [-1][(col * 2) + 1])
            media = int (soma / 2)
            imagem_ret [-1][col] = media

        for lin in range (linhas_ret - 1):

            soma = (imagem_original[lin * 2][-1]) + (imagem_original[(lin * 2) + 1][-1])
            media = int (soma / 2)
            imagem_ret[lin][-1] = media

        imagem_ret [-1][-1] = imagem_original [-1][-1]

    return imagem_ret

def main ():

    p2, colunas_img_o, linhas_img_o, valor_max, imagem_original, tipo_de_red = def_entradas ()

    if tipo_de_red == "retracao":
        imagem_retr = def_retracao (imagem_original)
        def_imprimir_imagem (imagem_retr)
    
    else:
        imagem_exp = def_expansao (imagem_original)
        def_imprimir_imagem (imagem_exp)

main ()

#    #    #
##   ##   ##
###  ###  ###