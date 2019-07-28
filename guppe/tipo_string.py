"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

"""

nome = 'felipe roschel'
print(nome)
print(type(nome))


nome = "felipe's roschel"
print(nome)
print(type(nome))

nome = 'felipe \nroschel'
print(nome)
print(type(nome))

nome = "felipe \" roschel"
print(nome)
print(type(nome))

nome = "felipe roschel"

print(nome.upper())
print(nome.lower())
print(nome.split()) # Transforma em uma lista de strings


nome = 'felipe roschel'
print(nome[0:4]) # Slice de string

nome = 'felipe roschel'
print(nome.split()[1])


nome = 'felipe roschel'
print(nome[::-1]) # Inverte a string

nome = 'felipe roschel'
print(nome.replace('f', 'r'))