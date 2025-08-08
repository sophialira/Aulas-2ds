turmas = {

    "2A": ["Ana", "Beatriz", "Diego", "Giovanni"],
    "2B": ["Eduarda", "Flávio", "Henrique", "Olívia"],
    "2C": ["Lara", "Nicolas", "Victor", "Pietro"]
}

while True:
    print("\nMenu: ")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Mostrar listas de alunos")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_aluno = input("Digite o nome do aluno: ")
        turma = input("Em qual turma ele(a) será colocado: ")
        if turma in turmas:
            turmas[turma] = nome_aluno
            print(f"Aluno {nome_aluno} foi adicionado na turma {turma}.")
        else:
            print("Turma inexistente.")

    elif opcao == 2:
        remover_aluno = input("Digite o nome do aluno para ser removido: ")
        if remover_aluno in turmas:
            del turmas[remover_aluno]
            print(f"Aluno {remover_aluno} removido.")

    elif opcao == 3:
        for turma, alunos in turmas.items():
            print(f"{turma}: ")
            for aluno in alunos:
                print(f" - {aluno}")

    elif opcao == 4:
        print("Fechando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")