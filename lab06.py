###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: Marcos Luan Moraes de Olievira  
# RA: 221532
###################################################

# Leitura de dados

sequencia = [int(i) for i in input().split()] # Cria uma lista com todos os numeros digitados, separados por espaço

numeros_rota = 0
senha = 1

while numeros_rota != 4: # Rotações

    numeros = len (sequencia)
    numeros_aux = 1
    numero_sequencia = 0
    sequencias_invalidas = 0 
    numeros_len = (len (sequencia) - 1)
    while numeros_aux < numeros:
        numero_ant = sequencia [numero_sequencia]
        numero_sequencia = numero_sequencia + 1
        numeros_len = numeros_len - 1
        if numeros_len == 0:
            break
        numero_pos = sequencia [numero_sequencia]
        if numero_ant > numero_pos:
            sequencias_invalidas = sequencias_invalidas + 1
            if sequencias_invalidas == 2:
                senha = 0
                numeros_rota = 3
                break
             
        numeros_aux = numeros_aux + 1
    
    numero_rodado = sequencia.pop (0)
    sequencia.append (numero_rodado)
    numeros_rota = numeros_rota + 1

if senha == 1 : 
    print ("Klift, Kloft, Still, a porta se abriu")
else:
    print ("Senha incorreta")