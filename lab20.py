###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 20 - Fuga de Nova York II
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
###################################################


'''
Dada uma matriz e a posição (x,y), realiza a 
verificação de é possível realizar a fuga da cidade
ou se é necessário o resgate aéreo.

def fuga(matriz, x, y):
#   ...

'''

# Leitura de dados

matriz = []

linha = input()

while not(linha.isnumeric()):
  matriz.append(linha.split())
  linha = input()

l = len (matriz)
c = len (matriz [0])

n = int(linha)


for i in range (n):
    x, y = [int(k) for k in input().split()]
    processamento = 0
    while True:

        if 0 <= x < l and 0 <= y < c:
            processamento = processamento + 1

            # processamento = processamento + 1
            # if processamento > (l * c):
            #     print ("Resgate aereo solicitado.")
            #     break
            coordenada_atual = matriz[x][y]



            
            coordenada_esquerda = matriz [x][y - 1]
            coordenada_cima = matriz [x - 1][y]

            if x == (l -1):
                print ("Fuga da cidade realizada.")
                break
            else:
                coordenada_baixo = matriz [x + 1][y]

            if y == (c - 1):
                print ("Fuga da cidade realizada.")
                break
            else:
                coordenada_direta = matriz [x][y + 1]


            if coordenada_atual == "H":

                if coordenada_direta == "N":
                    y = y - 1
                else:
                    if coordenada_direta == "H":
                        y = y - 1
                    else:
                        y = y + 1


            if coordenada_atual == "V":
                
                if coordenada_cima == "N":
                    x = x + 1
                else:
                    if coordenada_cima == "V":
                        x = x + 1
                    else:
                        x = x - 1
                    

            if coordenada_atual == "T":

                if coordenada_cima == "N":
                    if coordenada_cima == "V":
                        x = x + 1
                    if coordenada_baixo == "N":
                        if coordenada_direta == "N":
                            if coordenada_esquerda == "N":
                                print ("Resgate aereo solicitado.")
                                break
                            else:
                                if coordenada_esquerda == "T":
                                    y = y + 1
                                else:
                                    y = y -1
                        else:
                            if coordenada_direta == "T":
                                y = y - 1
                            else:
                                y = y + 1
                    else:
                        if coordenada_baixo == "T":
                            x = x - 1
                        else:
                            x = x + 1
                else:
                    if coordenada_cima == "T":
                        x = x + 1
                    else:
                        x = x - 1

                
                

            if coordenada_atual == "N":
                print ("Resgate aereo solicitado.")
                break

        else:
            print ("Fuga da cidade realizada.")
            break
    
    if processamento > (l * c):
        print ("Resgate aereo solicitado.")
        break







# Verifica se é preciso realizar a fuga da cidade
# ou solicitar o resgate aéreo para cada posição
#   ...



# H: a equipe pode se movimentar para a direita ou para a esquerda
# V: a equipe pode se movimentar para cima ou para baixo
# T: a equipe pode se movimentar para a direita, para a esquerda, para cima ou para baixo
# N: a equipe não pode se movimentar

#    #    #
##   ##   ##
###  ###  ###