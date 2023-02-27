# Estruturas de Controle e iteradores python

"""No python, possuímos as mesmas estruturas de controle e de lógica
de outras linguagens, porém com algumas particularidades...
"""
valor = 1
# "Se... senão..."
if type(valor) == int:
    print(valor)
    valor += 0.5
else:
    print("Valor não inteiro")

print(valor)
# "Se... senão se...
if type(valor) == int:
    print("Soma não efetuada")
elif type(valor) is not int:
    print(type(valor))

# "Para... "
lista = ["carro", "casa", "dinheiro", "fama"]

for a in range(len(lista)):
    print(a, lista[a])
    a += 1
    if a not in range(len(lista)):
        print(f'{a} fora do valor')

# "Enquanto..."
nome = input("Insira seu nome: ")
while nome:
    print(nome)
    if nome != "":
        break
