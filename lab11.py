###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
###################################################

# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 

nova_iorque = []
while True:
    entrada = input().split()
    if entrada[0].isnumeric():
        n_equipe = int(entrada[0])
        break
    else:
        nova_iorque.append(entrada)
        

# Leitura das coordenadas e início do processamento

n = len(nova_iorque)
m = len(nova_iorque[0])

for i in range(n_equipe):
    x, y = [int(k) for k in input().split()]
    caminho = []
    while True:
        if 0 <= x < n and 0 <= y < m:
            caminho.append([x, y])
            passo = nova_iorque[x][y]
            if passo == 'L':
                y = y + 1
            if passo == 'N':
                x = x - 1
            if passo == 'O':
                y = y - 1
            if passo == 'S':
                x = x + 1
        else:
            if y >= m:
                print("Fuga pelo leste.")
            if x < 0:
                print("Fuga pelo norte.")
            if y < 0:
                print("Fuga pelo oeste.")
            if x >= n:
                print("Fuga pelo sul.")
            break
        
        if [x, y] in caminho:
            print("Resgate aereo solicitado.")
            break




print ("Fim do programa ")

#   #   #
##  ##  ##
### ### ###     