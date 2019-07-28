"""

Try / Except / Else / Finally

- Toda entrada de dados deve ser tratada;


# Exemplos


num = None

try:
    num = int(input('informe um numero: '))
except:
    print('valor incorreto')
else:
    print(f'voce digitou {num}')


# Finally

try:
    num = input('informe um numero: ')
except ValueError:
    print('voce não digitou um valor válido')
else:
    print('depois do bloco try/except')
finally:
    print('executou o finally')

# Obs: O Blco finally é SEMPRE executado, independente se houve exceção ou não.

# O finally geralmente é utilizado para fechar ou desalocar recurso. Exemplo:
# desalocar uma conexão com o banco de dados, fechar um arquivo aberto para
# leitura por exemplo e etc;



# Exemplo ERRADO, os tratamentos devem ser feitos dentro da função

def dividir(a, b):
    return a / b

num1 = int(input('informe o primeiro numero: '))

try:
    num2 = int(input('informe o segundo numero: '))
except ValueError:
    print('o valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except ValueError:
    print('valor incorreto')



# Forma correta de fazer o tratamento específico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('valor incorreto')
    except ZeroDivisionError:
        return 'não é possível divisao por zero'

num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))


# Forma genérica

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'ocorreu um problema: {err}'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))

"""

