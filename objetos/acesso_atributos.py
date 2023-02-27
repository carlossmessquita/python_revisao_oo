"""Uma das principais implicações do Encapsulamento na OO é a segurança no acesso dos atributos
de uma classe. Os atributos e métodos de uma classe podem ter diferentes níveis de acesso, normalmente
sendo definidos como:

Públicos - Acesso livre para manipulação por elementos externos à classe.
Privados - Acesso restrito para manipulação, permitidos apenas para elementos internos à classe.

Podendo existir variações como os valores Protegidos, pouco usual em Python, mas que liberam
o acesso para manipulação dos elementos de uma classe por elementos inseridos no mesmo pacote apenas.

"""
class Alarme():
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def set_estado(self, valor: bool) -> None:
        self.__estado = valor

    def get_estado(self) -> bool:
        return self.__estado

