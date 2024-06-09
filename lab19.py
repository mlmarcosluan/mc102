###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 19 - Busca em Imagens
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
###################################################
"""
def flip_horizontal(img_A):
    

def flip_vertical(img_A):
    

def rotacao_180(img_A):
"""



def criaca_img ():

    p2 = input()

    m, n = input ().split () 

    n = int (n) # Numero de linhas da matriz
    m = int (m) # Numeros de colunas da matriz

    cor = int (input ())

    img = []
    
    for l in range (n):
        linha = input().split ()
        for i in range (m):
            linha[i] = int (linha[i])

            

        img.append (linha)

    return img


def verificar1 (img1, img2): #img_2 é a imagem rotacionada/flit/original/etc

    linhas1 = len (img1)
    colunas1 = len (img1[0])

    linhas2 = len (img2)
    colunas2 = len (img2[0])

    iguais = 0

    for i in range (linhas1):

        for j in range (colunas1):

            

            for l in range (linhas2):

                for c in range (colunas2):

                    item1 = img1[i + c][j + l]
                    item2 = img2[c][l]

                    if item1 != item2:
                        
                        iguais = 0
                        break
                    
                    else:
                        iguais = iguais + 1


    return iguais
    
                       


   


def rotacao_90(img):

    linhas = len (img)
    colunas = len (img[0])

    img_90 = []

    for i in range (colunas):
        linha = []
        for j in range (linhas):
            item = img[j][i]
            linha.append (item)

        img_90.append (linha)

    return img_90










def main ():

    img_A = criaca_img ()

    img_B = criaca_img ()

    rodar_90 = rotacao_90 (img_B)

    rodado_90 = verificar1 (img_A, rodar_90)
    original = verificar1 (img_A, img_B)


    



    print ("Fim do programa")



main ()



##    ###############    ##
###    ### ## ## ###    ###
####    ### # # ###    ####
#####    #### ####    #####
######    ### ###    ######
#######    ## ##    #######
########    ###    ########