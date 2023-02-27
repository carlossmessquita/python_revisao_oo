"""No Python, basicamente tudo é objeto e a origem dos objetos está nas classes
das quais derivam, isto é, os objetos são instâncias de classes que os moldam...

Classes são abstrações em código de objetos e seres do mundo real e são compostas por
atributos, que são características que identificam esse objeto real e métodos, são as
ações características deste objeto ou ser no domínio real.

Objetos são derivados de classes, numa relação similar aos moldes e seus produtos resultantes.
"""


class Pessoa():
    # Construtor(es) da classe
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        # Atributos públicos
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    # Métodos
    def se_apresentar(self):
        return f'Olá, eu sou {self.nome} {self.sobrenome} e tenho {self.idade} anos.'


class Cidadao(Pessoa):
    def __init__(self, Pessoa, cpf: str) -> None:
        self.nome = Pessoa.nome
        self.sobrenome = Pessoa.sobrenome
        self.idade = Pessoa.idade
        self.__cpf = cpf # Atributo privado

    def ver_cpf(self):
        print(self.__cpf)


class Animal():
     def __init__(self, tipo: str) -> None:
         self.tipo = tipo

# Classe Cachorro herda seu atributo 'tipo' da classe Animal
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str) -> None:
        self.nome = nome
        self.raca = raca
        self.tipo = "Doméstico"

    def se_apresenta(self):
        return f'Au au... Sou o {self.nome}, um cachorro {self.raca} e sou um animal {self.tipo}'

