"""

O bloco with é utilizando para criar um contexto de trabalho onde os recursos utilizados
após o bloco with são fechados.

"""


# Exemplo


# Forma Pythonica de manipular arquivos, dentro de contextos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)  # Arquivo ainda aberto pois está dentro do bloco with


print(arquivo.closed)  # Arquivo já fechado pois está fora do bloco with





