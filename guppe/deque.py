"""
Módulo Collections - Deque

- É uma lista de alta performance;
- Segue todos os métodos de uma lista praticamente;

"""

# Fazendo o import
from collections import deque

# Criando deques
deq = deque('felipe')
print(deq)

# Adicionando elementos no deque
deq.append('y') # Adicona o valor no final da lista
deq.appendleft('ç') # Adicona o valor no início da lista
print(deq)

print(deq.pop()) # Remove o último item da lista
print(deq.popleft()) # Remove o primeiro item da lista
