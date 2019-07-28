"""

**kwargs

Assim como no *args, poderíamos nomea-lo de qualquer coisa, mas por convenção
o denominamos por duploasteriscokwargs **kwargs.

Diferentemente do *args que coloca os valores extras em uma tupla
o **kwargs insere os parametros extras em um dicionario.

Sendo um dicionário, todas as possibilidades de um dicionário são aplicadas também
ao **kwargs!

"""

# Exemplo

"""
def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')


#  OBS: os parâmetros *args e **kwargs não são obrigatórios



def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'você recebeu um cumprimento pythonico!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek!"
    return 'não tenho certeza de quem vc é...'



print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))


# Nas funções, podemos ter:
#-parametros obrigatórios;
#-*args;
#-parametros default (não obrigatórios)
#-**kwargs
# OBS: Obrigatóriamente na ordem acima!


#  Exemplo:

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):  #  funcao declarada na ordem obrigatoria dos parametros
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'julia')  # apenas parametros obrigatorios
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)  # alem dos parametros obrigatorios, os 3 numeros vao para o *args e alterando o valor da var solteiro
minha_funcao(34, 'felipe', eu='não', voce='vai')  # alem dos parametros obrigatorios, passando tambem o **kwargs pois os valores estao declarados com chave e valor (eu='nao')
minha_funcao(39, 'carla', 9, 4, 3, java=False, python=True)  # todos parametros com exceção do default

"""


# Entendendo o porque é importante manter a ordem dos parâmetros

"""
# ordem correta
def mostra_info(a, b, *args, instrutor='geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='university', cargo='instrutor'))


# ordem incorreta
def mostra_info(a, b, instrutor='geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

#  Neste caso o valor de args e instrutor (default) ficam com o valor invertido entre-si
print(mostra_info(1, 2, 3, sobrenome='university', cargo='instrutor'))



# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'felicity', 'sobrenome': 'jones'}

print(mostra_nomes(**nomes))  # usando ** para desempacotar o dic

"""


