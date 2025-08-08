contatos = {

    "Arnaldo": "995632134",
    "Bianca": "987532150",
    "Caio": "907652367",
    "Douglas": "974021349"
}

while True:
    print("\nMenu:")
    print("1 - Adicionar contato")
    print("2 - Mostrar contatos")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_contato = input("Digite o nome da pessoa: ")
        adicionar_contato = int(input("Digite o número da pessoa: "))
        contatos[nome_contato] = adicionar_contato
        print(f"Contato de '{nome_contato}' foi adicionado.")

    elif opcao == 2:
        print(contatos)