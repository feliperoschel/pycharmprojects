"""
Loop while

- Utilizado para iterar sobre sequências, assim como loop for, porém de forma mais simples;
- É uma expressão booleana, que tem como condição de parada é a expressão booleana, enquanto
  ela for True, o loop se repete;
- Em um looping while é importante que cuidemos do critério de parada, para evitar o loopping
  infinito;

Obs.: Expressão booleana é toda expressão onde o resultado é Verdadeiro ou Falso;

"""

# Exemplo 1
numero = 1

while numero < 10:
    print(numero)
    numero += 1


# Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')


