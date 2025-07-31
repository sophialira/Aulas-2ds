class Aparelhos:
    def __init__(self, conexao, sistemaoperacional, processador, memoria):
        self.__conexao=conexao
        self.__sistemaoperacional=sistemaoperacional
        self.__processador=processador
        self.__memoria=memoria

class PC (Aparelhos):
    def __init__(self, conexao, sistemaoperacional, processador, memoria):
        self.__conexao=conexao
        self.__sistemaoperacional=sistemaoperacional
        self.__processador=processador
        self.__memoria=memoria

computador = PC("Wifi", "Windows 11", "Intel i7", "1TB")

print(computador.__memoria)
