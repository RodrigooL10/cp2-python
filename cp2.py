# -*- coding: utf-8 -*-
import sys
from sys import exit

# criando tipos de vinho, quantidade e preços

estoque = [["Vinho tinto", 50, 35.90],
           ["Vinho branco", 20, 29.99],
           ["Vinho rosé", 15, 24.50],
           ["Vinho espumante", 26, 42.00],
           ["Vinho do porto", 45, 55.00]]

compras = []

id_compra = 0

# criando menu
while True:
    print("----- MENU PRINCIPAL -----")
    print("1. Menu de Estoque")
    print("2. Menu de Compras")
    menu = int(input("Digite qual menu deseja acessar: "))
# criando menu para escolha estoque
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
                    print("----- Estoque -----")
                    print("Produto | Quantidade | Valor")

                    for vinho, quantidade, preco in estoque:
                        print(f"{vinho} | {quantidade} | R${preco:.2f}")

                    print("----- Fim do Estoque -----\n")
# criando codigo para adicionar produtos no estoque
                case 2:
                    print("----- Registrar Entrada -----")
                    nome = input("Digite o nome do produto: ")
                    quantidade = int(input("Digite a quantidade: "))

                    for i in range(len(estoque)):
                        vinho = estoque[i][0]
                        qtd_vinho = estoque[i][1]

                        if vinho == nome:
                            qtd_vinho += quantidade
                            estoque[i][1] = qtd_vinho
                            print(estoque)
                            break
                        else:
                            valor = float(input("Digite o valor do produto: "))
                            estoque.append([nome,quantidade,valor])
                            print(estoque)
                            break

                    print("\n----- Fim do Registro de Entrada -----\n")
# criando codigo para retirada de produtos no estoque 
                case 3:
                    print("----- Registrar Saída -----")
                    nome = input("Digite o nome do produto: ")
                    quantidade = int(input("Digite a quantidade: "))

                    encontrou_item = False
                    for i in range(len(estoque)):
                        vinho = estoque[i][0]
                        qtd_vinho = estoque[i][1]

                        if vinho == nome:
                            qtd_vinho -= quantidade
                            estoque[i][1] = qtd_vinho
                            print(estoque)
                            encontrou_item = True
                            break


                    if not encontrou_item:
                        print("Produto não encontrado no estoque")

                    print("\n----- Fim do Registro de Saída -----\n")

                case 0:
                    print("Voltando ao menu principal...\n")
                    break

# criando codigo para compra e carrinho
    elif menu == 2:
        while True:
            print("----- Menu de Compras -----")
            print("1. Cadastrar compra")
            print("2. Mostrar todas as compras")
            opcao_compras = int(input("Digite a opção desejada: "))


            if opcao_compras == 1:
                cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")
                descricao = input("Digite a descrição da compra: ")
                quantidade = int(input("Digite a quantidade da compra: "))
                valor_unitario = float(input("Digite o valor unitário da compra: "))
                valor_total = quantidade * valor_unitario
                id_compra += 1
                compra = {"cnpj_fornecedor": cnpj_fornecedor, "descricao": descricao,
                          "quantidade": quantidade, "valor_unitario": valor_unitario,
                          "valor_total": valor_total}
                compras.append(compra)

            elif opcao_compras == 2:
                print("Todas as compras:")
                for compra in compras:
                    print(f"--Id da Compra: {id_compra}--")
                    print("CNPJ do fornecedor:", compra["cnpj_fornecedor"])
                    print("Descrição:", compra["descricao"])
                    print("Quantidade:", compra["quantidade"])
                    print("Valor unitário:", compra["valor_unitario"])
                    print("Valor total:", compra["valor_total"])
