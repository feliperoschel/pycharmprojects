"""
Saindo de loops com break

Utilizado para sair de loops de maneira projetada

"""

# Exemplo 1 - For
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)

print('Sai do loop')



# Exemplo 1 - while
while True:
    comando = input("Digite 'sair' para sair:")
    if comando == 'sair':
        break

print('Sai do loop')
