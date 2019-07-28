"""
- Precisamos conhecer o loop for para usar os ranges;
- Precisamos conhecer o range para trabalhar melhor com loops for;
- Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim
  de maneira especificada;
- Formas gerais: range(valor_de_parada), o Valor de parada é não inclusivo
  (início padrão 0, e o passo de 1 em 1)

"""

# Exemplo Forma 1 - Não especificando o início, ele começa com 0;
for num in range(11):
        print(num)


# Exemplo Forma 2 - Especificando valor
for num in range(1, 5):
        print(num)


# Exemplo Forma 3 - Passo maior que 1
for num in range(1, 10, 2):
        print(num)


# Exemplo Forma 4 - Inversa
for num in range(10, 0, -1):
        print(num)
