"""
Definindo Funções

- Criar partes do código que executam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- São úteis para executar procedimentos similares por repetidas vezes;
    - DRY - Don't Repeat Yoursel

Obs.: Se você escrever uma função e realiza várias tarefas dentro dela
é interessante fazer uma verificação para que a função seja simplificada

- Já utilizamos funções no decorrer do curso, exemplo:
    - print();
    - len();
    - max();
    - min();
    - count();
    - entre várias outras;

- Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função
através da variável
"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando funções integradas (built-in) do python:
print(cores) # Imprime um valor
cores.append('roxo') # Adiciona um valor á lista
print(cores)


"""
A forma geral para definir uma função é:
    def nome_da_funcao(parametros_de_entrada):
        bloco_da_funcao

onde: 
nome_da_funcao -> SEMPRE, com letras minúsculas e separadas por underline quando o nome for composto (Snake case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, devem ser separados por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função ocorre;
"""

# Definindo a primeira função

# Exemplo 1

# Dentro de uma função, podemos utilizar outras funções;
# Esta função executa uma única tarefa;
# Também não recebe nenhum parâmetro de entrada;
# Não retorna nada também
def diz_oi():
    print('oi!')

# Utilizando funções - Chamando a execução da função
diz_oi()


# Exemplo 2
def cantar_parabens():
    print('parabéns pra você...')

cantar_parabens()
cantar_parabens()
cantar_parabens()
cantar_parabens()

# Ou executar um loop para não repetir a chamada das funções
for n in range(5):
    cantar_parabens()

print('******')

# Executar função através de variável - NÃO RECOMENDADO
canta = cantar_parabens()
canta()

