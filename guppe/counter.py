"""
Módulo Collections - Counter (Contador)

Collection -> High-performance container datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Countes
que é parecido com um dicionário, contendo como chave o elemento da lsita passando como parâmetro
e como valor a quantidade de ocorrências desse elemento

"""

# Utilizando o counter

from collections import Counter

# Podemos utilizar qualquer iterável, neste exemplo usamos lista mas poderia ser tupla, dicionário, conjunto etc;
lista = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]

# Exemplo 1
res = Counter(lista) # Retorna para cada elemento da lista, é criada uma chave e indica como valor a quantidade de ocorrências do valor
print(type(res))
print(res)


# Exemplo 2
print(Counter('felipe roschel'))


# Exemplo 3
texto = """Resident Evil 5 is a third-person shooter video game developed and published by Capcom, and produced by Jun Takeuchi (pictured). It was released for PlayStation 3 and Xbox 360 consoles on March 5, 2009. The plot involves an investigation of a terrorist threat by counter-terrorist agents Chris Redfield and Sheva Alomar in Kijuju, a fictional region of Africa. It is the seventh major installment in the Resident Evil series, and the first designed for two-player cooperative gameplay. Critics described the game as closer to the action genre than the survival horror of other games in the series. Resident Evil 5 had a mostly positive reception, although it was criticized for problems with its controls. The game was re-released for Nvidia Shield, PlayStation 4 and Xbox One in 2016. As of September 2018, it had sold over 7.4 million units, making it Capcom's second best-selling game and the best-selling game of the Resident Evil franchise. (Full article...) """
print(Counter('felipe roschel'))

palavras = texto.split()
#print(palavras)

print('-------')
res = Counter(palavras)
print(res)

print('////')
# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

