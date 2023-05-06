""" Grupo:
    - Guilherme Dejulio - RM550295
    - Marcelo Tan - RM551771
    - Rodrigo Lima - RM98326
"""

import sys
from sys import exit

# criando estoque com alguns produtos e suas quantidades
estoque = [["Garrafa tipo A", 500],
           ["Garrrafa tipo B", 200],
           ["Rolha", 150],
           ["Rótulo", 260],
           ["Uva", 450]]

compras = []

id_compra = 0

# criando menu principal
while True:
    print("\n----- MENU PRINCIPAL -----")
    print("1. Menu de Estoque")
    print("2. Menu de Compras")
    menu = int(input("Digite qual menu deseja acessar: "))

    # criando menu de estoque
    if menu == 1:
        while True:
            print("\n----- Menu de Estoque -----")
            print("1. Exibir estoque")
            print("2. Registrar Entrada")
            print("3. Registrar Saída")
            print("0. Voltar ao Menu Principal")
            menu2 = int(input("Digite qual opção deseja acessar: "))

            # exibindo estoque
            match menu2:
                case 1:
                    print("\n----- Estoque -----")
                    print("Produto | Quantidade ")

                    for produto, quantidade in estoque:
                        print(f"{produto} | {quantidade}")

                    print("----- Fim do Estoque -----\n")

                # criando codigo para adicionar produtos no estoque
                case 2:
                    print("\n----- Registrar Entrada -----")
                    nome = input("Digite o nome do produto: ")
                    quantidade = int(input("Digite a quantidade: "))

                    for i in range(len(estoque)):
                        produto = estoque[i][0]
                        qtd_produto = estoque[i][1]

                        if produto == nome:
                            qtd_produto += quantidade
                            estoque[i][1] = qtd_produto
                            break
                        else:
                            estoque.append([nome,quantidade])
                            break
                    print("Produto Registrado com sucesso")
                    print("----- Fim do Registro de Entrada -----")

                # criando codigo para retirada de produtos no estoque
                case 3:
                    print("\n----- Registrar Saída -----")
                    nome = input("Digite o nome do produto: ")
                    encontrou_item = False

                    for i in range(len(estoque)):
                        produto = estoque[i][0]
                        qtd_produto = estoque[i][1]

                        if produto == nome:
                            quantidade = int(input("Digite a quantidade: "))
                            qtd_produto -= quantidade
                            estoque[i][1] = qtd_produto
                            encontrou_item = True
                            print("A quantidade de produto foi removida com sucesso")
                            print("\n----- Fim do Registro de Saída -----")
                            break

                    if not encontrou_item:
                        print("Produto não foi encontrado no estoque")
                #Voltando ao menu principal
                case 0:
                    print("\nVoltando ao menu principal...")
                    break

    # criando menu de compras
    elif menu == 2:
        while True:
            print("\n----- Menu de Compras -----")
            print("1. Cadastrar compra")
            print("2. Mostrar todas as compras")
            print("0. Voltar ao Menu Principal")
            opcao_compras = int(input("Digite a opção desejada: "))

            match opcao_compras:

                # Cadastrando compra
                case 1:
                    print("\n-- Cadastrando compra --")
                    cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")
                    descricao = input("Digite a descrição da compra: ")
                    quantidade = int(input("Digite a quantidade da compra: "))
                    valor_unitario = float(input("Digite o valor unitário da compra: "))
                    valor_total = quantidade * valor_unitario
                    id_compra += 1
                    compra = {"id": id_compra, "cnpj_fornecedor": cnpj_fornecedor, "descricao": descricao,
                              "quantidade": quantidade, "valor_unitario": valor_unitario,
                              "valor_total": valor_total}
                    compras.append(compra)
                    print("Compra foi cadastrada com sucesso!")
                    print("\nVoltando ao menu de compras...")

                #Exibindo compras realizadas
                case 2:
                    print("\n-- Exibindo todas as compras: --")
                    for compra in compras:
                        print("\n-- Id da Compra:", compra["id"], "--")
                        print("CNPJ do fornecedor:", compra["cnpj_fornecedor"])
                        print("Descrição:", compra["descricao"])
                        print("Quantidade:", compra["quantidade"])
                        print("Valor unitário:", compra["valor_unitario"])
                        print("Valor total:", compra["valor_total"])
                    print("\n-- Fim de todas as compras realizadas --")

                #Voltando ao menu principal
                case 0:
                    print("\nVoltando ao menu principal...")
                    break
