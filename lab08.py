###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: Marcos Luan Moraes de Oliveira  
# RA: 221532
###################################################

# DEFs
def verificacao (lis_primer, lis_fita, posi):
    letra = 0
    posi2 = 0
    while posi2 < (len (lis_primer)):
        if posi < len (lis_fita):

            if lis_primer [posi2] == "A":
                if lis_fita [posi] == "T": 
                    letra = letra + 1
                    posi = posi + 1

                else: 
                    return False
                    break

            elif lis_primer [posi2] == "C":
                if lis_fita [posi] == "G":
                    letra = letra + 1
                    posi = posi + 1

                else: 
                    return False
                    break

            elif lis_primer [posi2] == "G":
                if lis_fita [posi] == "C":
                    letra = letra + 1
                    posi = posi + 1

                else: 
                    return False
                    break
            

            elif lis_primer [posi2] == "T":
                if lis_fita [posi] == "A":
                    letra = letra + 1
                    posi = posi + 1

                else: 
                    return False
                    break
        
        
            posi2 = posi2 + 1

        else:
            return False
            break

    if letra == (len (lis_primer)):
        return True
    else:
        return False


# Leitura de dados
fita = input () # Entrada da fira de DNA
primer = input () # Entrada da sequencia do primer


# Verificação da ligação dos primers na fita


# Criando uma lista com o input da fita e do primer
lis_fita = list (fita)
lista_primer = list (primer)

lis_primer = lista_primer [::-1]



aux = 0
aux2 = 0
lis_primer.remove ("5")
lis_primer.remove ("3")
lis_fita.remove ("5")
lis_fita.remove ("3")


posi = 0
posi_valida = []

while posi < (len  (fita) - 2):
    if verificacao (lis_primer, lis_fita, posi):
        posi_valida.append (posi)
    posi = posi + 1



            



    


# Impressão da saída do programa
aux = 0
if len (posi_valida) > 0:
    while aux < len (posi_valida):
        print ("Ligacao na posicao", (posi_valida [aux])+ 1)
        aux = aux + 1
else:
    print ("Nenhuma ligacao")

#   #   #
##  ##  ##
### ### ###