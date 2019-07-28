"""

Sorted

OBS: Não confunda com a função sort que já estudamos em Listas. O Sort só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável e serve para ordenar as coleções.

# Exemplos

numeros = [6, 1, 8, 2]

print(numeros)
print(sorted(numeros))  # Ele gera uma nova lista e ordena conforme definido.
print(numeros)  # Veja que neste exemplo a ordem continua conforme a variável, pois o comando sorted() não altera a lista. Já o sort, altera a lista, então nas próximas utilizações a lista estará modificada.


numeros = [6, 1, 8, 2]

print(numeros)

print(sorted(numeros))

print(sorted(numeros, reverse=True))


# Podemos utilizar o sorted() para coisas mais complexas. Exemplo:


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username
print(sorted(usuarios, key=lambda usuario: usuario['username']))  # Se executar sem a key, gera erro, pois exige chave de ordenação
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))  # Também é possível utilizar demais parametros como o reverse

# Ordenando pelo numero de tweets ascendente
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']))) # Também é possível utilizar demais parametros como o reverse



musicas = [
    {"título": "thunderstruck", "tocou": 3},
    {"título": "dead skin mask", "tocou": 2},
    {"título": "back in black", "tocou": 4},
    {"título": "litle birds", "tocou": 8}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))


"""

