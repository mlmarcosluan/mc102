###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: Marcos Luan Moraes de Oliveira  
# RA: 221532
###################################################

# Leitura de dados
t = int (input ())
dist_a = int (input ()) 
vel_a = float (input ()) 
t_pit_stop = float (input ())
dist_b = int (input ())
vel_b = float (input ())




# Cálculo do tempo total gasto para realizar o pit stop
t_a = (dist_a * 3600) / (vel_a * 1000) # t_a é o tempo que o carro leva do ponto de entrada até o pitstop
t_b = (dist_b * 3600) / (vel_b * 1000) # t_b é o tempo que o carro leva do pitstop até a saida do box

soma = t_a + t_b + t_pit_stop
 

# Impressão da resposta
print (soma < t )

#    #    #
##   ##   ##
###  ###  ###
