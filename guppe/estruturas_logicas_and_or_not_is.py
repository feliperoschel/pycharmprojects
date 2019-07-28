"""
Estruturas Lógicas

-> and, or, not, is;

Operadores unários:
    -> not, is
Operadores binários:
    -> and, or

and - ambas condições precisam ser atendidas;
or - uma das condições precisa ser atendida;
not - o valor do booleano é invertido, true, vira false, e vice-versa;

"""

ativo = False
logado = True

if not ativo:
    print('Ative sua conta, cheque seu email')
else:
    print('Bem vindo usuário')

print(ativo is False)


nome = 'felipe'
print(nome.istitle()) # Testa se var nome is title

