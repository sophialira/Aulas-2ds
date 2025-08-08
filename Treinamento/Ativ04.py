lista_de_compras = {

    "Frutas": ["Maçã", "Banana", "Abacaxi"],
    "Carnes": ["Frango", "Carne Suína"],
    "Verduras": ["Alface", "Couve", "Espinafre"],
    "Lacticínios": ["Leite", "Iogurte"],
    "Limpeza": ["Sabão em pó", "Detergente", "Limpa-vidros"]
}

print("Lista de compras agrupada: \n")
for categoria, itens in lista_de_compras.items():
    print(f"{categoria}: ")
    for item in itens:
        print(f" - {item}")
    print ()