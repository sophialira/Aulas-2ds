class Wifi:
    def __init__ (self, senha, nome):
        self._senha= senha
        self._nome= nome

Acesso = Wifi("1234567890", "E.E. Carlos Gomes")

print(Acesso._senha)
print(Acesso._nome)

