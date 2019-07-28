"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Import This - Easter Egg (Poema Python)

A idéia da PEP8 é que possamos escrever códigos Python de forma Pythônica, ou seja
agradável;


[1] - Utilize Camel Case para nomes de Classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma_dois():
    pass


[3] - Utilize 4 espaços para identação! (Não use tab);


[4] - Linhas em branco:
      - Separar funções e definições de clase com duas linhas em branco;
      - Métodos dentro de uma classe devem ser separados com uma única linha em branco;


[5] - Imports
      - Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import_sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo após quaisquer comentários
ou docstrings, antes de constantes ou variáveis globais;


[6] - Espaços em expressões e instruições;

# Não faça:

funcao( algo[1 ], { outro: 2 } )
algo (1)
dict ['chave'] = list (indice)

# Faça:

funcao(algo[1], {outro: 2})
algo(1)
dict('chave') = lista[indice]


[7] - Termine sempre uma instrução com uma nova linha, ou seja, dando enter para
ficar posicionado em uma nova linha;

"""


