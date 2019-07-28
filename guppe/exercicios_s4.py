"""
Exercícios - Seção 4


# 1 Faça um programa que leia um número inteiro e imprima
numint = 5
print(numint)

# 2 Faça um programa que leia um número real e imprima
numint = 5.23
print(numint)

# 3 solicite ao usuário que digite 3 valores inteiros e imprima sua somatória
soma = 0
qtde = 3
for n in range(1, qtde + 1):
    vlrret = int(input('Informe um valor inteiro: '))
    soma = soma + vlrret

print(f'A soma é {soma}')

# 4 Leia um número real e imprima o resultado do quadrado deste número
vlrrea = 1.25
print(f'A soma é: {vlrrea * 2}')

# 5 Leia um número real e imprima a quinta parde deste número
vlrrea = 6
print(f'A quinta parte é: {vlrrea / 5}')

# 6 Leia a temperatura em Celsius e apresente-a convertida para Fahrenheit
celsius = 28
print(f'A temperatura: {celsius} em Celsius é: {celsius *(9 / 5) + 32} em Fahrenheit')

# 7 Leia a temperatura em Fahrenheit e apresente-a convertida para Celsius
fahrenheit = 99
print(f'A temperatura: {fahrenheit} em Fahrenheit é: {5 * (fahrenheit - 32) / 9} em Celsius')

# 8 Leia a temperatura em Kelvin e apresente-a convertida para Celsius
kelvin = 120
print(f'A temperatura: {kelvin} em Kelvin é: {kelvin - 273.15} em Celsius')

# 9 Leia a temperatura em Celsius e apresente-a convertida para Kelvin
celsius = 38
print(f'A temperatura: {celsius} em Celsius é: {celsius + 273.15} em Kelvin')

# 10 Leia a velocidade em km/h e apresente-a convertida para m/s (metros por segundo)
velocidade = 50
print(f'A velocidade: {velocidade} em Km/h corresponde à: {velocidade / 3.6} em Metros por Segundo')

# 11 Leia a velocidade em m/s e apresente-a convertida para km/h
velocidade = 200
print(f'A velocidade: {velocidade} em M/S corresponde à: {velocidade * 3.6} em KM/H')

# 12 Leia uma distância em milhas e apresente-a convertida para km
distancia = 153
print(f'A distância: {distancia} em milhas corresponde à: {distancia * 1.61} em km')

# 40
qtde_dias = int(input('Informe quantos dias serão trabalhados: '))
valor_dia = 30
print(f'o Valor Líquido à pagar é: {(valor_dia * qtde_dias) - (((valor_dia * qtde_dias) * 8) / 100)}')

# 44
import math

altura_degrau = 13 #cm
altura_desejada = 1000 #cm
print(f'{math.ceil(altura_desejada / altura_degrau)}') # https://docs.python.org/3.7/library/math.html?highlight=math#module-math

# NAO RESOLVIDO 45 Convertento valores LOWER/UPPER utilizando a tabela ASC
nome = 'felipe'
#print(ascii(nome))
for code in nome.encode('ascii'):
    print(code)


# 46 - Inverter um numero
numero = input('Insira um número para ser invertido: ')
print(int(str(numero)[::-1]))


# 52

felipe = 50
denis = 30
bigatto = 40
total = felipe + denis + bigatto
felipe_percentual = (felipe / total) * 100
denis_percentual = (denis / total) * 100
bigatto_percentual = (bigatto / total) * 100
print(f'Felipe receberia: % {round(felipe_percentual, 2)} do prêmio')
print(f'Denis receberia: % {round(denis_percentual, 2)} do prêmio')
print(f'Bigatto receberia: % {round(bigatto_percentual, 2)} do prêmio')

"""

"""
nome = ''
apostadores = ()
valor = 0
while nome != 'sim':
    nome = input('Informe o nome do apostador: ')
    valor = float(input('Informe o valor apostado: '))
    apostadores = {'Nome': nome, 'Valor': valor}
    apostadores ['nome'] = nome, ['valor'] = valor
    receita['abr'] = 350
    print(apostadores)
    """

"""felipe = 50
denis = 30
bigatto = 40
total = felipe + denis + bigatto
felipe_percentual = (felipe / total) * 100
denis_percentual = (denis / total) * 100
bigatto_percentual = (bigatto / total) * 100
print(f'Felipe receberia: % {round(felipe_percentual, 2)} do prêmio')
print(f'Denis receberia: % {round(denis_percentual, 2)} do prêmio')
print(f'Bigatto receberia: % {round(bigatto_percentual, 2)} do prêmio')
"""