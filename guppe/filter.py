"""

Filter


Filtrar dados de uma determinada coleção


# Exemplos


# Forma Comum

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)



# biblioteca para trabalhar com estatísticas
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)
print(media)

# Vamos filtrar os valores acima da media dada acima
# Assim como a função map, a função filter também recebe dois parametros, função e iterável

print(f'Média: {media}')

res = filter(lambda x: x > media, dados)  # seleciona apenas os valores maiores que a media

print(list(res))

print(type(res))

print(f'novamente: {list(res)}')   #  Assim como na função map, após a execução, o valor é zerado, portanto esta linha será uma lista vazia, pois são excluídos da memória



# Retirar os países nulos da lista através de Filter.

paises = ['', 'argentina', '', 'brasil', 'chile', '', 'colombia']
print(paises)

res = filter(None, paises)

print(list(res))



# A diferença entre map e filter é que:

# map() - recebe dois parametros, uma função e um iterável, e retorna um objeto mapeando a função para cada elemento do iteravel

# filter() - recebe dois parametros, uma função e um iterável, e retorna um objeto filtrando os elementos de acordo com a função



# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

#print(usuarios)

# Filtrar os usuários que estão inativos no twitter


# Forma 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)


# Forma 2 - Utilizando bool
inativos = list(filter(lambda usuario: not len(usuario['tweets']), usuarios))
print(inativos)


# Combinar filter() e map()

nomes = ['vanessa', 'ana', 'maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + o nome, desde que cada nome tenha menos que 5 caracteres

lista = list(map(lambda nome: f'Sua Instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)


"""


