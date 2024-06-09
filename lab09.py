####################################################
# MC102 - Algoritmos e Programação de Computadores #
# Laboratório 9 - Controle de Estoque 2.0          #
# Nome: Marcos Luan Moraes de Oliveira             #
# RA: 221532                                       #
####################################################


### 666 ###





def def_entrada():

    entrada = input ()
    if entrada == "FIM":
        return "FIM"
    
    else:
        entrada = entrada.split(":")
        entrada[0] = entrada[0].strip()
        entrada[1] = int (entrada[1].strip())
        return entrada

def def_verifica (estoque, entrada, compra, venda):

    if entrada == "FIM":
        return estoque, entrada, compra, venda
    else:
        produto = entrada[0]
        numero = entrada[1]

        if numero > 0: # Adiciona ao estoque

            if produto in estoque: # O produto ja esta no estoque
                estoque[produto] = estoque[produto] + numero
            else: # O produto não esta no estoque
                estoque[produto] = numero

            if produto in compra: # Já foi feito uma compra
                compra[produto] = compra[produto] + 1

            else: # Ainda não foi feito uma compra
                compra[produto] = 1


        else: # É uma venda

            if produto in estoque: # Existe o produto no estoque
                if estoque[produto] >= abs (numero): # O numero do estoque é maior que o numero da venda
                    estoque[produto] = estoque[produto] + numero
                    if produto in venda: # Ja foi veito uma venda
                        venda[produto] = venda[produto] + 1
                    else: # Ainda não foi feito uma venda
                        venda[produto] = 1

                else: # O numero do estoque é menor que o pedido de venda
                    print("Quantidade indisponivel para a venda de " + str(abs(numero)) + " unidade(s) do produto " + produto + ".")

            else: # Não há produto no estoque
                print("Quantidade indisponivel para a venda de " + str(abs(numero)) + " unidade(s) do produto " + produto + ".")

    return estoque, entrada, compra, venda



def main ():

    estoque = {}
    compra = {}
    venda = {}

    lista_produtos = []

    entrada = def_entrada ()


    while entrada != "FIM":
        
        estoque, entrada, compra, venda = def_verifica (estoque, entrada, compra, venda)

        entrada = def_entrada ()

    
    lista_produtos = []

    for produto in estoque:

        lista_produtos.append (produto)

    lista_produtos = sorted (lista_produtos)


    for produto in lista_produtos:
        if produto not in venda:
            venda[produto] = 0
        if produto not in compra:
            compra[produto] = 0




    for i in range (len (lista_produtos)):
        print("Produto: " + lista_produtos[i])
        print("Quantidade em Estoque: " + str (estoque[lista_produtos[i]]))
        print("Pedidos de Compra: " + str (compra[lista_produtos[i]]))
        print("Pedidos de Venda: " + str (venda[lista_produtos[i]]))
    
    

    
main ()













### 666 ###
