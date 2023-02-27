# Revisão de Python Básico

"""Tipos Primitivos em Python

Basicamente em Python podemos ter os seguintes tipos primitivos:

1. int (inteiro)
2. float (decimal)
3. str (textual)
4. bool (lógico/booleano)
5. None (vazio)
"""

num_int = 1
print(type(num_int))

num_float = 3.5
print(type(num_float))

txt = "Olá, meu nome é Carlos"
print(type(txt))

val_bool = True
print(type(val_bool))

vazio = None
print(type(vazio))

"""Além dos tipos primitivos, podemos ter algumas estruturas de dados básicas

1. list (Lista de valores indexados, variados e mutável)
2. tuple (Tupla de valores indexados, não variados e imutável)
3. dict (Dicionários de valores ordenados por chave-valor e mutável)
"""

lista = ["Carlos", "Mesquita", 23]
print(f'{lista[0]}, {lista[1]}, {lista[2]}')
print(type(lista))

tupla = ("altura", 1.76)
print(f'{tupla[0]},{tupla[1]}')
print(type(tupla))

dicio = {"nome":"Carlos", "idade":23}
print(f'{dicio["nome"]}, {dicio["idade"]}')
print(type(dicio))