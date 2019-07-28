"""

StringIO

- Para ler ou escrever dados em arquivos do SO, o software precisa de permissão para tal;

- Utilizado para ler e crar arquivos em memória;


"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'teste é uma string normal'

arquivo = StringIO(mensagem)

# agora tendo o arquivo, podemos utilizar todas as funções de manipulação de arquivos
# que conhecemos nas aulas anteriores

print(arquivo.read())

arquivo.write('novo texto')

arquivo.seek(0)

print(arquivo.read())