"""
Dicionários

Obs: Em algumas linguagens, os dicionários são conhecidos por mapas;

- São coleções do tipo Chave/Valor;
- São representados por chaves {} ex: print(type{}))
- São separados por Chave e Valor - 'chave:', 'valor';
- Podem receber qualquer tipo de dados;
- A forma de adicionar ou atualizar dados em um dicionário é a mesma;
- Em dicionários NÃO podemos ter chaves repetidas
"""

# Exemplo 1 - Mais comum e recomendado
paises = {'br:', 'brasil', 'eua:', 'estados unidos', 'py:' 'paraguai'}
print(paises)

# Exemplo 2 - Menos comum
paises = dict(br='brasil', eua='estados unidos', py='paraguai')
print(paises)


# Acessando elementos

# 1 - Acessando via chave
paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}
print(paises['br'])
print(paises['py'])


# 2 - Acessando via get *** RECOMENDADA pois não retorna erro caso a chave não exista
print(paises.get('br'))
print(paises.get('ru'))

russia = paises.get('py')
pais = paises.get('py')
pais = paises.get('px', 'não encontrado') # já trata o retorno caso não encontrada a chave, retornando o valor pre estabelecido para a variável (Valor Padrão)

if russia:
    print(f'encontrei o pais {pais}')
else:
    print('NÃO encontrei o pais')

# Verificar se a chave se encontra em determinado dicionário
print('br' in paises)
print('ru' in paises)
print('estados unidos' in paises) # a busca é feita por CHAVE e NÃO valor!

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado, int float, string, boolean, lista, tuple etc
# Exemplo, tuplas sendo utilizada para definição de chave de dicionário
# é uma utilização interessante, pois são imutáveis

localidades = {
    (35.6895, 39.6917): 'escritório em tókio',
    (40.7128, 74.0060): 'escritório em nova york',
    (37.7749, 122.4194): 'escritório em são paulo',
}
print(localidades)


# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

print('------')
# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

print('------')

# Forma 2
novo_dado = {'mai': 350}
receita.update(novo_dado)
print(receita)


# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

print('**********')
# Como remover dados de um dicionário

# Forma 1 - mais comum
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print('/////')
ret = receita.pop('mar') # pop remove o último elemento e retorna o valor removido
print(ret)

# Forma 2
del receita['fev'] # remove  elemento, porém não retorna o valor removido;
print(receita)

"""
Por que utilizar dicionário? :
imagine a situação de um ecommerce, um carrinho de produtos

Carrinho de Compras:
Produto 1:
    - nome;
    - qtde;
    - preço
Produto 2:
    - nome;
    - qtde;
    - preço
"""

# 1 - Poderíamos utilizar uma Lista para isso? SIM

carrinho = []

produto1 = ['game 1', 1, 230.50]
produto2 = ['game 2', 1, 120.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto, exemplo:
# Indice 0 = produto; índice 1 = preço; índice 2 = valor etc


# 1 - Poderíamos utilizar uma Lista para isso? SIM

carrinho = []

produto1 = ['game 1', 1, 230.50]
produto2 = ['game 2', 1, 120.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto, exemplo:
# Indice 0 = produto; índice 1 = preço; índice 2 = valor etc


# 1 - Poderíamos utilizar uma Tupla para isso? SIM

produto1 = ('game 1', 1, 230.50)
produto2 = ('game 2', 1, 120.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto, assim como na lista;


print("////////")


# Utilizando dicionário - mais recomendada para a situação, pois fica claro o que é cada valor, já que você insere um dicionário para os itens

carrinho = []

produto1 = {'nome': 'game 1', 'quantidade': 1, 'valor': 230.50}
produto2 = {'nome': 'game 2', 'quantidade': 1, 'valor': 120.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)



# Métodos de dicionários
print(dir({}))

# Limpando os dados de um dicionário
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
d.clear()
print(d)

print('--------')
# Copiando um dicinoário par aoutro

# Forma 1 - Deep copy

novo = d.copy()

novo['d'] = 4
print(d)
print(novo)

print('/////////////////')
# Forma 2 - Shallow copy

novo = d
print(novo)

novo['d'] = 5
print(d)
print(novo)


# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

print('-----------')
# O método fromkeys recebe dois parametros: intervalo e valor
# Ele vai gerar para cada valor do iterável, uma chave e irá atribuir a esta chave o valor informado, no exemplo abaixao o valor será 'desconhecido'
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)


# Neste exemplo ele irá considerar cada letra como uma chave
# t: valor; e: valor e assim sucessivamente;
# como as chaves não podem ser repetidas, as letras serão impressas apenas uma vez
veja = {}.fromkeys('teste', 'valor')
print(veja)

print('-----')

# utilizando Range
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)