###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Marcos Luan Moraes de Oliveira
# RA: 221532
###################################################

# Leitura de dados
Score = int (input ()) 
Idade = int (input ())
Saldo = float (input ())
Salario = float (input ())

# Verificação se o cartão de crédito será concedido ou não

if Score >=300 and Score < 600:
    if Idade >= 30:
        if Salario >= 3000:
            if Saldo >= 7000:
                print ("Cartao concedido")
            else: # Saldo < 7000
                print ("Cartao nao concedido")
        else: #Salario < 3000
            print ("Cartao nao concedido")
            
    else: # Idade < 30
        print ("Cartao nao concedido")
elif Score >= 600:
    if Idade >= 50:
        print ("Cartao concedido")
    else: # Idade < 500
        if Salario >= 2000:
            print ("Cartao concedido")
        else: # Salario < 2000
            if Saldo >= 5000:
                print ("Cartao concedido")
            else: # Saldo < 5000
                print ("Cartao nao concedido")
else: # Score < 300
    print ("Cartao nao concedido")

    


