####################################################
# MC102 - Algoritmos e Programação de Computadores #
# Laboratório 13 - Eleições 2022                   #
# Nome: Marcos Luan Moraes de Oliveira             #
# RA: 221532                                       #
####################################################

def def_input ():
    
    # Pegaremos os imputs que são digitados linha a pos linha e adicionando eles numa lista

    lista_votos = []

    voto = input ()

    while voto != "0": # Enquanto o input dos votos for diferente de 0 a repetição continuara
        lista_votos.append (voto)
        voto = input () # Pede novamente para que seja digitado um novo voto

    return lista_votos

def def_dic_votos (lista_votos): # Função para transformar a lista de votos em um dicionario com os nomes dos candidatos e os numeros de votos

    dic_votos = {}

    for voto in range (len (lista_votos)): # Percorre por todos os votos da lista de votos

        voto_atual = lista_votos [voto]

        if voto_atual not in dic_votos: # Pergunta se o candidato do voto atual ainda não esta no dicionario
            dic_votos [voto_atual] = 1

        else: # Caso o candidato do voto atual ja esteja no dicionario apenas soma + 1
            dic_votos [voto_atual] += 1

    
    brancos = dic_votos.pop ("Branco")
    nulos = dic_votos.pop ("Nulo")

    return dic_votos, brancos, nulos

def def_organiza (dic_votos):

    tuplas_candidatos_votos = list(dic_votos.items ())

    for final in range (len (tuplas_candidatos_votos), 0, -1):

        trocas = False

        for atual in range (0, final -1):

            atual_t = tuplas_candidatos_votos[atual][1]
            proximo_t = tuplas_candidatos_votos[atual + 1][1]

            if atual_t < proximo_t:
                tuplas_candidatos_votos[atual], tuplas_candidatos_votos[atual + 1] = tuplas_candidatos_votos[atual + 1], tuplas_candidatos_votos[atual] 
                
                trocas = True

        if not trocas:
            break

        
    return tuplas_candidatos_votos





def main ():

    lista_votos = def_input () # Entradas

    dic_votos, brancos, nulos = def_dic_votos (lista_votos) # Cria um dicionario com os nomes dos candidatos e os seus votos

    tuplas_organizada = def_organiza (dic_votos)

    for i in range (len (tuplas_organizada)):

        print (tuplas_organizada[i][0], tuplas_organizada[i][1])

    print ("Brancos", brancos)
    print ("Nulos", nulos)

main ()

#    #    #
##   ##   ##
###  ###  ###