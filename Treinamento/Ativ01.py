alunos = {
    "Ana": [9, 10, 8, 5, 7],
    "Breno": [2, 3, 5, 5, 0],
    "Carlos": [10, 6, 6, 7, 8],
    "Daniele": [0, 10, 9, 8, 8],
    "Eduardo": [1, 3, 4, 6, 7],
    "Flávia": [5, 5, 6, 7, 8]
}

medias = {}
for nome, notas in alunos.items():
    medias[nome] = sum(notas) / len(notas)

for nome, media in medias.items():
    print(f"{nome}: {media:.2f}")

