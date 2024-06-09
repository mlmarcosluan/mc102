#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 18 - Jogos Olímpicos
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
#####################################################

def medalhas_paises ():
    N, O, P, B = [int(x) for x in input().split()]

    medalhas = {}

    for i in range (N):
        aux = input ().split()
        medalhas[aux[0]] = aux[1], aux[2], aux[3]

    return medalhas, O, P, B


def posi (medalhas, esportes):
        
    ouro = []
    prata = []
    bronze = []

    for i in range (len(esportes)):
        medalha_ouro = medalhas[esportes[i]][0]
        ouro.append (medalha_ouro)

        medalha_prata = medalhas[esportes[i]][1]
        prata.append (medalha_prata)

        medalha_bronze = medalhas[esportes[i]][2]
        bronze.append (medalha_bronze)

    return ouro, prata, bronze


def def_paises (medalhas, esportes):

    paises = []

    for i in range (len (medalhas)):

        for x in range (3):

            aux1 = esportes[i]
            aux2 = medalhas[aux1][x]

            if aux2 not in paises :

                paises.append (aux2)
            
    
    return paises

    
def pontos (paises, ouro, prata, bronze, O, P, B):

    pontos_por_pais = {}

    for i in range (len (paises)):

        pais = paises[i]
        aux = ouro.count (pais)
        ponto = aux * O

        aux = prata.count (pais)
        ponto = ponto + (aux * P)

        aux = bronze.count (pais)
        ponto = ponto + (aux * B)

        pontos_por_pais[pais] = ponto

    return pontos_por_pais


def vencedor (paises, pontos_totais):

    vencedores = []
    parcial = 0
    pais_parcial = "brasil"

    for i in range (len (paises)):
        
        pais = paises[i]
        ponto = pontos_totais[pais]
            
        if ponto >= parcial:
            parcial = ponto
            pais_parcial = pais


    for i in range (len (paises)):

        pais = paises[i]
        ponto = pontos_totais[pais]

        if parcial == ponto:
            vencedores.append (pais)
                
    return vencedores

                
def main ():

    medalhas, O, P, B = medalhas_paises ()

    esportes = list(medalhas.keys ())

    ouro, prata, bronze = posi (medalhas, esportes)

    paises = def_paises (medalhas, esportes)

    pontos_totais = pontos (paises, ouro, prata, bronze, O, P, B)

    finalista = vencedor (paises, pontos_totais)
    finalista.sort()
    
    

    # pontos_esporte = ouro_finali (medalhas, finalista, ouro, esportes)
    

    
    
    for i in range (len (finalista)):
        pais = finalista[i]
        ponto = pontos_totais[pais]

        print (pais, ponto)

        if pais in ouro:
            for i in range (len (esportes)):
                aux = esportes[i]
                if pais in medalhas[aux][0]:
                    print (aux)







main ()

#   #   #
##  ##  ##
### ### ###