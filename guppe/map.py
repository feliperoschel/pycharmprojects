"""

Map

Com map, fazemos mapeamento de valores para uma função

# Exemplo


import math


def area(r):
    #Calcula a area de um circulo com raio 'r'
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))


# Forma comum

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)


# Forma 2 - Map
areas = map(area, raios)  # map é uma função que recebe dois parametros, primeiro a função, depois um iteravel
print(list(areas))
print(type(areas))
print(list(areas))


# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

print(areas)  ## IMPORTANTE: após utilizar a função map() depois da primeira utilização do resultado, ele zera, neste exemplo, o valor anterior é mostrado, porem o desta linha já está vazio.

# Para fixar MAP

# Temos dados iteráveis:
  # dados: a1, a2, ..., an
# temos uma função:
  # funcao: f(x)
# Utilizamos a funcao map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar uma função.
# O Map Object: f(a1), f(a2), f(...), f(an)

# Exemplo de cidades com temperaturas

cidades = [('berlin', 29), ('tokio', 27), ('cairo', 36), ('buenos aires', 19), ('londres', 22)]

print(cidades)

# Conversão para Fereh
# formula: f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5 * dado[1] + 32))
print(list(map(c_para_f, cidades)))


"""

