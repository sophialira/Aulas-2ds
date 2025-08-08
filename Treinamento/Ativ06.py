texto = input("Digite um texto: ")

palavras = texto.lower().split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("\n Contagem de palavras:")
for palavra, qtd in contagem.items():
    print(f"- {palavra} foi repetida {qtd} de vezes")