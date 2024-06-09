###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 17 - Vacinação AstraZeneca
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
###################################################



def def_doses (N):
    

    doses = []
    for i in range (N):
        aux = int (input ()) # Dose para cada mes
        doses.append (aux)

    return doses


def doses_suficiente (N, doses_mes, mes_atual):

    ### Return 0: Não há doses suficiente
    ### Return 1: Há doses suficinete 
    ### Return 2: Passou da nossa amostragem, Vacinar todos com D1

    if mes_atual + 3 > N: # Passou da nossa amostragem, Vacinar todos com D1
        return 2

    else: # Ainda temos mes adiante para analizar
        doses_atual = doses_mes[mes_atual - 1]
        doses_3meses = doses_mes[mes_atual + 2]

        if doses_atual <= doses_3meses: # Temos doses suficiente
            return 1
        
        else: # Não temos doses suficiente
            return 0


























def main ():

    N = int (input ()) # Nume de meses a ser analizados

    doses_mes = def_doses (N)

    D1 = [] # Numero de pessoas vacinadas com a primeira dose
    D2 = [] # Numero de pessoas vacinadas com a segunda dose
    X = []  # Numero de doses devolvidas
    apenas_D1 = []
    for i in range (N):
        D1.append (0)
        D2.append (0)
        X.append (0)
        apenas_D1.append (0)

    if N > 3: # Temos que analizar se existe doses suficiente
        mes_atual = 1

        

        while mes_atual <= N: 
            suficiente = doses_suficiente (N, doses_mes, mes_atual)

            if suficiente == 0: # Não há doses suficiente
                valor_mes_atual = doses_mes[mes_atual - 1] # Doses do mes atual
                valor_mes_3 = doses_mes[mes_atual + 2] # Doses daqui 3 meses
                D1.pop (mes_atual - 1)
                D1.insert (mes_atual - 1, valor_mes_3)
                D2.pop (mes_atual + 2)
                D2.insert (mes_atual + 2, valor_mes_3)
                X.pop (mes_atual - 1)
                X.insert (mes_atual - 1, (valor_mes_atual - valor_mes_3))
                doses_mes.pop (mes_atual + 2)
                doses_mes.insert (mes_atual + 2, 0)

                

            elif suficiente == 1: # Há doses suficinete
                valor_mes_atual = doses_mes[mes_atual - 1] # Doses do mes atual
                valor_mes_3 = doses_mes[mes_atual + 2] # Doses daqui 3 meses
                D1.pop (mes_atual - 1)
                D1.insert (mes_atual -1 ,valor_mes_atual)
                D2.pop (mes_atual + 2)
                D2.insert (mes_atual + 2, valor_mes_atual)

                doses_mes.pop (mes_atual + 2)
                doses_mes.insert (mes_atual + 2, (valor_mes_3 - valor_mes_atual))
            else: # Passou da nossa amostragem, Vacinar todos com D1
                D1.pop (mes_atual - 1)
                D1.insert (mes_atual - 1, doses_mes[mes_atual -1])
                apenas_D1.pop (mes_atual - 1)
                apenas_D1.insert (mes_atual - 1, doses_mes[mes_atual - 1])


            mes_atual = mes_atual + 1

        

    else: # Não precisamos analizar, basta dar todas as doses para D1
        for i in range (N):
            aux = doses_mes[i]
            D1.pop (i)
            D1.insert(i, aux)
            apenas_D1.pop (i)
            apenas_D1.insert (i, aux)



    
    for i in range(N):
        print("Mes " + str(i+1) + ":")
        print("Vacinados com a primeira dose:", D1[i])
        print("Vacinados com a segunda dose:", D2[i])
        print("Vacinas devolvidas:", X[i])

    soma_D1 = sum (apenas_D1)
    soma_D2 = sum (D2)
    soma_X = sum (X)
    print ("Total:")
    print ("Vacinados apenas com a primeira dose:", soma_D1)
    print ("Vacinados com as duas doses:", soma_D2)
    print ("Vacinas devolvidas:", soma_X)
    
main ()




#   #   #
##  ##  ##
### ### ###
