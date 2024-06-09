####################################################
# MC102 - Algoritmos e Programação de Computadores #
# Laboratório 4 - Avatar                           #
# Nome: Marcos Luan Moraes de Oliveira             #
# RA: 221532                                       #
####################################################

# Inicialização das variáveis
entrada = 0
water = 0
fire = 0
earth = 0
air = 0


# Leitura da sequência de treinamento
while entrada != "X":
    entrada = (input ())
    if entrada == "W": # O treinamento foi de Agua (Water)
        W_pontos = float ( input ())
        water = water + W_pontos

        if fire - (W_pontos / 2) > 0 :
            fire = fire - (W_pontos / 2)

        else:
            fire = 0

    elif entrada == "F": # O treinamento foi de Fogo (Fire)
        F_pontos = float ( input ())
        fire = fire + F_pontos

        if water - (F_pontos / 2) > 0 :
            water = water - (F_pontos / 2)
        
        else:
            water = 0
            

    elif entrada == "E": # O treinamento foi de Terra (Earth)
        E_pontos = float ( input ())
        earth = earth + E_pontos

        if air - (E_pontos / 2) > 0 :
            air = air - (E_pontos / 2)
        
        else:
            air = 0

    elif entrada == "A": # O treinamento foi de Ar (Air)
        A_pontos = float ( input ())
        air = air + A_pontos

        if earth - (A_pontos / 2) > 0 :
            earth = earth - (A_pontos / 2)
        
        else:
            earth = 0



# Impressão das informações de saída

print("Pontuacao Final")
print("Agua: {:.1f}".format(water))
print("Terra: {:.1f}".format(earth))
print("Fogo: {:.1f}".format(fire))
print("Ar: {:.1f}".format(air))


if water != 0 and earth != 0 and fire != 0 and air != 0:
    print ("Treinamento realizado com sucesso.")

else:
    print ("Realize mais treinamentos.")

#    #    #
##   ##   ##
###  ###  ###
