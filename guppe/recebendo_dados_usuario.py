"""

Recebendo dados do usuário:

input() -> t odo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:

"""


# Entrada de dados
#print("Qual seu nome? ")
#nome = input()
nome = (input('Qual seu nome?'))


#print("Qual sua idade? ")
#idade = input()
idade = int(input('Qual sua idade?'))


# Saída de Dados
# print(f'Seja bem-vindo(a) {nome}')
# nome = nome.lower().title()
print(f'O {nome.lower().title()} tem {idade} anos e nasceu em {2018 - idade}')

