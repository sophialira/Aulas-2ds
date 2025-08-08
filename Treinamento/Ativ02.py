estoque = {
    "Perfume": [35, 25],
    "Hidratante Corporal": [30, 42],
    "Batom": [7, 30],
    "Maquiagem": [15, 18]
}

while True:
    print("\nMenu:")
    print("1 - Remover um produto")
    print("2 - Adicionar um novo produto")
    print("3 - Mostrar estoque")
    print("4 - Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_remover = input("Digite o nome do produto que deseja remover: ")
        if nome_remover in estoque:
            del estoque[nome_remover]
            print(f"Produto '{nome_remover}' removido com sucesso.")
        else:
            print("Produto não encontrado no estoque.")

    elif opcao == 2:
        nome_produto = input("Digite o nome do novo produto: ")
        qtd = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
        estoque[nome_produto] = [qtd, preco]
        print(f"Produto '{nome_produto}' adicionado com sucesso.")

    elif opcao == 3:
        print("\nEstoque Atual:")
        for produto, dados in estoque.items():
            print(f"{produto}: Quantidade: {dados[0]}, Preço: R${dados[1]:.2f}")

    elif opcao == 4:
        print("Fechando programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")