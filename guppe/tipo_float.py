"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.

"""

# Errado do ponto de vista do Float, pois gera uma Tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista do Float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter float para int, porém perdemos precisão
res = int(valor)
print(res)
print(type(res))


# Podemos trabalhar com números complexos
variavel = 5j

