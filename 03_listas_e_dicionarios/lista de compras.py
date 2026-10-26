produtos =[]
continuar = True
while continuar:
    print("===========LISTA DE COMPRAS===========")
    print("1 - Adicionar produto")
    print("2 - Mostar produtos")
    print("3 - Remover produto")
    print("4 - Sair")
    print("5 - Limpar lista")
    opcao = input("Escolha uma opção: ")
    if  opcao == "1":
        produto = input("Digite o nome do produto: ")
        produtos.append(produto)
        print("Produto adicionado com sucesso!")
    elif opcao == "2":
        print("======PRODUTOS=======")
        if len(produtos) == "0":
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)
    elif opcao == "3":
        produto = input("Digite o produto que deseja remover: ")
        if produto in produtos:
            produtos.remove(produto)
            print("Produtp removido com sucesso!")
        else:
            print("Produto não encontrado.")
    elif opcao == "4":
        print("Encerrando o sistema...")
        continuar = False
    elif opcao =="5": 
        produtos.clear()
        print("Lista limpa com sucesso!")
    
