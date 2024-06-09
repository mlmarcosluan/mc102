######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
######################################################################

# Leitura do número de meses

N = int(input()) # Quantos meses seram analizados pelo programa

# D2 Pessoas completamente imunizadas
# D1 Pessoas imunizadas com a primeira dose
# D2A Pessoas que receberam a segunda dose com atraso
# D1A Pessoas esperando a primeira dose com atraso

n_meses = 0 
doses_mes = []
while n_meses < N:
    dose =  int (input ()) # Numero de doses
    doses_mes.append(dose)
    n_meses = n_meses + 1

D1 = 0
D2 = 0
D2A = 0
D1A = 0

mes_atrasado = 0
mes_atrasado2 = 0

# Calculos

primeira_dose = 0
segunda_dose = 0
segunda_dose_atrasada = 0

aux = N

while aux > 0:
    doses_do_mes = doses_mes [0]
    
    while doses_do_mes > 0: # Ainda exite dose para o mes atual

        if segunda_dose_atrasada > 0: # Exite pessoas com a 2 dose atrasada

            if segunda_dose_atrasada <= doses_do_mes: # Tem mais doses do que pessoas
                 doses_do_mes = doses_do_mes - segunda_dose_atrasada
                 D2 = D2 + segunda_dose_atrasada 
                 D2A = D2A + segunda_dose_atrasada
                 segunda_dose_atrasada = 0
            
            else: # Tem mais pessoas que doses
                segunda_dose_atrasada = segunda_dose_atrasada - doses_do_mes
                D2 = D2 + doses_do_mes
                D1 = segunda_dose_atrasada
                D2A = D2A + doses_do_mes
                doses_do_mes = 0


        elif primeira_dose > 0: # Pessoas pronta para tomar a 2 dose
            if primeira_dose <= doses_do_mes: # Tema mais doses do que pessoas
                doses_do_mes = doses_do_mes - primeira_dose
                D2 = D2 + primeira_dose
                primeira_dose = 0
                D1 = 0
                

            else: # Tem mais pessoas que doses
                segunda_dose_atrasada = primeira_dose - doses_do_mes
                D2 = D2 + doses_do_mes
                D1 = primeira_dose - doses_do_mes
                primeira_dose = 0
                doses_do_mes = 0
                
            
                
        else: # Não exite doses em atrasos
            primeira_dose = doses_do_mes
            D1 = primeira_dose
            doses_do_mes = 0
        
        

    doses_mes.remove(doses_mes[0]) 

    if aux == 1: # Estamos no ultimo mes do programa 
        D1A = segunda_dose_atrasada

    if segunda_dose_atrasada > 0: # Pessoas com a segunda dose vencida no final do mes
        mes_atrasado = mes_atrasado + 1

    else:
        mes_atrasado = 0


    if mes_atrasado > 1:
        D1A = segunda_dose_atrasada
        mes_atrasado = 0



    

    aux = aux - 1


      


# Impressão da saída

print("Pessoas completamente imunizadas:", D2)
print("Pessoas imunizadas apenas com uma dose:", D1)
print("Pessoas que tomaram a segunda dose com atraso:", D2A)
print("Pessoas esperando a segunda dose com atraso:", D1A)

#   #   #
##  ##  ##
### ### ###