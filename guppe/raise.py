"""

Levantando os próprios erros com raise

- Lança exceções;
- Não é uma função, é uma palavra reservada;
- Serve para criarmos nossas próprias mensagens de erro;

Sintaxe:
raise tipodoerro('mensagem de erro')



# Exemplo

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'o texto {texto} será impresso na cor {cor}')

colore('felipe', 4)



def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in (cores):
        raise ValueError(f'a cor precisa ser uma entre {cores}')
    print(f'o texto {texto} será impresso na cor {cor}')

colore('felipe', 'roxo')


Obs.: O raise assim como o return, finaliza a função, ou seja, nada após ele é executado;

"""

