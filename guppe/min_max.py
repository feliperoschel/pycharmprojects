"""

Min e Max


max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos;

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos;


# Exemplos


lista = [1, 8, 4, 99, 34, 129]  # funciona para listas, tuplas, set, dic etc;

print(max(lista))

dicionario = {'a': 1, 'b': 8, 'c': 4}

print(max(dicionario))
print(max(dicionario.values()))

# Faça um programa que recebe dois valores do usuário e mostre o mario

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))


print(max(4, 65, 3))

print(max('a', 'g', 'h'))

print(max(3.145, 5.789))

print(max('felipe roschel'))


min()  # Extamente igual a todos os exemplos do max();



nomes = ['arya', 'samson', 'dora', 'tim', 'ollivander']

print(max(nomes))  # tim - pois a consideração é mediante as letras do alfabeto

print(min(nomes))  # arya - pois a consideração é mediante as letras do alfabeto


print(max(nomes, key=lambda nome: len(nome)))  # baseado no tamanho da string e não mais na ordem alfabetica

print(min(nomes, key=lambda nome: len(nome)))  # baseado no tamanho da string e não mais na ordem alfabetica



musicas = [
    {"título": "thunderstruck", "tocou": 3},
    {"título": "dead skin mask", "tocou": 2},
    {"título": "back in black", "tocou": 4},
    {"título": "litle birds", "tocou": 8}
]


print(max(musicas, key=lambda musica: musica['tocou']))

print(min(musicas, key=lambda musica: musica['tocou']))


# Imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['título'])

print(min(musicas, key=lambda musica: musica['tocou'])['título'])


# Como encontrar a musica mais e menos tocada sem usar max min e lambda?

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['título'])


min = 99999

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['título'])

"""



