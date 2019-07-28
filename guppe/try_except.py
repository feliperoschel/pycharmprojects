"""
O block try/except

- Utilizamos para tratar erros que possam ocorrer em nosso código, prevenindo que o programa
pare de funcionar e o usuário recebe uma mensagem de erro inesperada;


A forma geral mais simples é:


try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema



# Exemplos

try:
    geek()
except:
    print('deu algum problema')


Obs.: Tratar erro de forma genérica não é a melhor forma. Tentar tratar de forma
específica.


# Erro específico

try:
    len(5)
except TypeError:
    print('você está utilizando uma função inexistente')


# Erro específico

try:
    len(5)
except TypeError as err:   # dando um apelido ao erro, no Python é comum usar 'err'
    print(f'a aplicação gerou o seguinte erro: {err}')


try:
    #len(5)
    #geek()
    print('felipe'[9])
except NameError as erra:
    print(f'deu nameerror: {erra}')
except TypeError as errb:
    print(f'deu typerror: {errb}')
except:
    print('deu um erro nao catalogado')



def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': 'geek'}

print(pega_valor(dic, 'teste'))


"""
