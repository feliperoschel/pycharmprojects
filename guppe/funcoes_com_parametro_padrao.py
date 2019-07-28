"""
Funções com Parâmetros Padrão (Default Parameters)

Sâo funções onde a passagem de parâmetros é opcional

print('felipe roschel')

print()  # funcao passada sem parâmetro, porém é executada normalmente, ou seja, o parâmetro é opcional



def quadrado(numero):
    return numero ** 2


print(quadrado(3))

print(quadrado())  # exemplo de função onde o parâmetro é obrigatório, caso contrário, retorna erro



# Definindo um valor padrão para o argumento, e ele é considerado como padrão caso não seja passado nenhum valor padrão para o parâmetro

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # Utiliza o 3 como parâmetro (valor passado pelo usuário)

print(exponencial(3))  # Por padrão eleva ao quadrado, que foi definido na função e não gera erro

print(exponencial())  # utiliza ambos valores padrão da função


#  OBS: Em funções Python os parâmetros com valor default devem estar SEMPRE ao final da declaração, exemplo:

def def_teste(num = 1, potencia) # Erro de compilação!


# Outros exemplos

# nos permite ser mais flexiveis com o uso das funções
# evita erros com parametros incorretos
# permite trabalhar com exemplos mais legiveis no codigo


def mostra_informacao(nome='geek', instrututor=False):
    if nome == 'geek' and instrututor:
        return 'bem-vindo instrutor geek!'
    elif nome =='geek':
        return 'eu pensei que era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrututor=True))
print(mostra_informacao('ozzy'))
print(mostra_informacao(nome='stef'))



# Exemplo de funcão sendo utilizada como parâmetro:


def soma(num1, num2):   # funcao de soma
    return num1 + num2


def mat(num1, num2, fun=soma):   # utiliza a funcao soma no terceiro parametro
    return fun(num1, num2)  # faz a chamada da funcao soma passando os parametros da funcao incial


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))  # utiliza a funcao soma que é a padrao da funcao mat para terceiro parametro
print(mat(2, 2, subtracao))  # troca a funcao soma por funcao subtracao da funcao mat, logo, o resultado sera a execucao da funcao subtracao



# Escopo - Evitar problemas e confusões


# Variáveis globais
# Variáveis locais

instrutor = 'geek'  # variavel global

def diz_oi():
    instrutor = 'python'  # variavel local
    return f'Oi {instrutor}'


print(diz_oi())
print(diz_oi())  # se tivermos uma variavel local com o mesmo da variavel global, a local terá preferencia, ou seja, ela será utilizada


def diz_oi():
    prof = 'geek'  # variavel local
    return f'Oi {prof}'


print(diz_oi())
print(prof)  # é gerado erro pois a variavel é local, e a funcao print neste formato, esta dependente de uma variavel global

# ATENCAO, sempre que puder evitar variavel global, evite!



total = 0  # Variavel global

def diz_oi():
    global total  # avisando que queremos utilizar uma variavel global, caso nao seja declarada, irá gerar erro not trecho abaixo pois a variavel nao foi declarada e já esta sendo utilizada para um processamento.
    total = total + 1
    return total


print(diz_oi())
print(diz_oi())  # importante lembrar que o valor da variavel global TOTAL neste caso, fica carregada em memoria com o valor da ultima execucao.



# Podemos ter funções que são declaradas dentro de funções e também possuem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador  # sinaliza que a variavel é uma NÃO LOCAL, ou seja, nao local e não global, está atrelada à funçao anterior

        contador = contador + 1
        return contador
    return dentro()  # chama a funcao dentro e retorna o resultado dela

print(fora())
print(fora())
print(fora())  # Neste exemplo o contador é zerado a cada execução, diferentemente do exemplo anterior que nao zeramos a variavel a cada execucao, ficando com o valor carregado em memoria.

"""

