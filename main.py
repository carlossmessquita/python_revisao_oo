from objetos import Classe

carlos_pessoa = Classe.Pessoa("Carlos", "Mesquita", 23)
print(carlos_pessoa.se_apresentar())

carlos_cidadao = Classe.Cidadao(carlos_pessoa, "***.987.546-**")
carlos_cidadao.ver_cpf()
print(carlos_cidadao.se_apresentar())

cao = Classe.Cachorro("Toto", "Vira-Lata")
print(cao.se_apresenta())


