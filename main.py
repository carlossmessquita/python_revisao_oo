from objetos import Classe, acesso_atributos

carlos_pessoa = Classe.Pessoa("Carlos", "Mesquita", 23)
print(carlos_pessoa.se_apresentar())

carlos_cidadao = Classe.Cidadao(carlos_pessoa, "***.987.546-**")
carlos_cidadao.ver_cpf()
print(carlos_cidadao.se_apresentar())

cao = Classe.Cachorro("Toto", "Vira-Lata")
print(cao.se_apresenta())

al = acesso_atributos.Alarme(False)
print(al.get_estado())
al.set_estado(True)
print(al.get_estado())

