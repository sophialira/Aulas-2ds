while True:
    ("\n Menu: ")
    print("1 - Média dos alunos")
    print("2 - Sorteio")
    print("3 - Percorrer matriz")
    print("4 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        n1 = int(input("Nota 1: "))
        n2 = int(input("Nota 2: "))
        n3 = int(input("Nota 3: "))
        n4 = int(input("Nota 4: "))
        soma = (n1 + n2 + n3 + n4)
        media = (soma / 4)
        print(f"A média do aluno é: {media}")

    elif opcao == 2:
        import random
        nomes_dos_alunos = ["Alice", "Henry", "Helena", "Luan", "Rafaela", "Pietro"]
        sorteado = random.choice(nomes_dos_alunos)
        print(f'Aluno sorteado foi: {sorteado}')

    elif opcao == 3:
        matriz = [

            [12, 14, 16],
            [20, 21, 22],
            [33, 44, 55]
        ]
        for linha in matriz:
            print(linha)