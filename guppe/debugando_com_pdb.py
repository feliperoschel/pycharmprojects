"""

Debugando com PDB

PDB: Python Debugger



# Exemplos


def dividir(a, b):
    print(f'a= {a}, b={b}')  # a utilização do print no meio do código NÃO é uma boa prática
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'ocorreu um problema: {err}'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))


# Existe formas mais profissionais de se fazer o debug
# Em python podemos fazer isso utilizando diferentes IDEs
# o PDB - Python Debugger


# Exemplo com PyCharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'ocorreu um problema: {err}'

num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))

# Obs.: Ao ativar o debug, selecionando o trecho e com botão direito é possível 'add to watch list' onde o trecho será monitorado, no exemplo acima, foi feito no trecho da dividação a/b



# Exemplo com o PDB
# Para utilizar o PDB precisamos importar a biblioteca PDB e então utilizar a função set_trace()

# Comandos básicos PDB:
  #- l (listar onde estamos no código
  #- n (pŕoxima linha)
  #- p (imprime variável)
  #- c (continua a execução - finaliza o debug)


Obs.: A partir do python 3.7 não e necessário importar a biblioteca pdb
pois o debug foi incorporado como função built-in chamada breakpoint()

import pdb

nome = 'felipe'
sobrenome = 'roschel'
pdb.set_trace()    # break point manual do pdb
nome_completo = nome + ' ' + sobrenome
curso = 'programacao python'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Porque utilizar este formato via PDB?
# O debug é utilizado durante o desenvolvimento, após a identificação
# do problema e correção, o import e trace é removido do código

nome = 'felipe'
sobrenome = 'roschel'
import pdb; pdb.set_trace()    # break point manual do pdb, sem importar previamente a biblioteca
nome_completo = nome + ' ' + sobrenome
curso = 'programacao python'
final = nome_completo + ' faz o curso ' + curso
print(final)


nome = 'felipe'
sobrenome = 'roschel'
breakpoint()  # Utilização sem fazer o import, apenas no Python 3.7+
nome_completo = nome + ' ' + sobrenome
curso = 'programacao python'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Obs.: Cuidado com conflitos entre nomes de variáveis e os comandos do PDB,
# neste caso, quando coincidir os nomes, utilize o comando p (nome da variavel) antes
# p <nome_variavel>, exemplo p n


"""


