###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
###################################################

# Leitura dos dados

N = int(input())

# Listas dos números de vacinados com a primeira e segunda dose em cada mês

D1 = []
D2 = []


# Lista do número de vacinas devolvidas em cada mês

X = []

doses_mes = [] # Lista com os numeros de doses para cada mes

# Processamento dos dados


# Criação da lista com os numeros de doses para cada mes ###
for doses in range (N): 
    doses = int (input ()) 
    doses_mes.append (doses)


# Se tivermos apenas 3 meses todas as doses vão para a 1° dose
if N ==3 : # Temos só 3 meses para analizar
    mes = 0
    while mes < 3:
        n_doses = doses_mes [mes]
        D1.append (n_doses)
        X.append (0)
        D2.append (0)
        mes = mes + 1

else: # Temos mais de 3 meses para analizar
    mes = 0
    while mes < N:
        n_doses = doses_mes [mes]
        if (mes + 3) < N: # Podemos analizar daqui 3 meses
            n_doses3 = doses_mes [mes + 3]

            if n_doses <= n_doses3: # Temos doses sofuciente para dar a todos a 2° dose
                if mes > 2: 
                    n_doses_passadas = doses_mes [mes - 3]
                    if n_doses - n_doses_passadas >= 0:
                        D1.append (n_doses - n_doses_passadas)
                        X.append (0)
                    else:
                        D1.append (n_doses)

                else:
                    D1.append (n_doses)
                    X.append (0)

            else: # Não temos doses suficiente para dar para todos a 2° dose
                D1.append (n_doses3)
                X.append (n_doses - n_doses3)

        else: # Não podemos analizar daqui 3 meses
            n_doses_passadas = doses_mes [mes - 3]
            if n_doses - n_doses_passadas <= 0:
                D1.append (0)
                X.append (0)
            else:
                D1.append (n_doses - n_doses_passadas)
                X.append (0)
        
        if mes > 2: # Podemos dar a 2° dose
            n_doses_passadas = doses_mes [mes - 3]
            if n_doses_passadas > n_doses: # Não temos todas as doses 2° dose
                D2.append (n_doses)

            else: # Não temos doses suficiente para 2° dose
                D2.append (n_doses_passadas)

        else: # Ainda não podemos dar a segunda dose
            D2.append (0)
        mes = mes + 1

# Impressão do uso das vacinas mês a mês

# for i in range(N):
#     print("Mes " + str(i+1) + ":")
#     print("Vacinados com a primeira dose:", D1[i])
#     print("Vacinados com a segunda dose:", D2[i])
#     print("Vacinas devolvidas:", X[i])
mes = 1
while mes <= N:
    print ("Mes ", mes,":", sep="")
    print ("Vacinados com a primeira dose:", D1[mes - 1])
    print("Vacinados com a segunda dose:", D2[mes - 1])
    print("Vacinas devolvidas:", X[mes - 1])
    mes = mes + 1

# Impressão do resumo final
total_primeira = (sum (D1)) - (sum  (D2))
total_segunda = (sum (D2))
total_devolvidas = (sum (X))

print ("Total:")
print ("Vacinados apenas com a primeira dose:", total_primeira)
print ("Vacinados com as duas doses:", total_segunda)
print ("Vacinas devolvidas:", total_devolvidas)

#   #   #
##  ##  ##
### ### ###