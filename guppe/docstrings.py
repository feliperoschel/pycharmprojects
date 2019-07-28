"""
Documentando funções com Docstrings

"""

# Exemplos

def diz_oi():
    """ Uma função simples que retorna a string 'oi!' """
    return 'Oi!'

# Executar via terminal help(diz_oi) será retornado a documentação da função que digitamos acima.

""""
Exemplo:
>>> from docstrings import diz_oi
>>> diz_oi()
'Oi!'
>>> print(diz_oi.__doc__)
 Uma função simples que retorna a string 'oi!' 
>>> 
"""