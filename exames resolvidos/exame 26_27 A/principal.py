# 2. b) (1,5 valores)
# Crie um módulo denominado principal.py que importe a classe Titular, crie dois objetos com dados
# distintos e apresente o nome e o NIF ofuscado de cada titular.
#
# 2. c) (1,0 valor)
# Apresente o resultado da validação para cada objeto criado.

from titular import Titular

titular1 = Titular("Ana Silva", "245123678")
titular2 = Titular("Carlos Pereira", "12345678")

print(titular1.nome, titular1.ofuscar_nif(), titular1.validar_nif())
print(titular2.nome, titular2.ofuscar_nif(), titular2.validar_nif())
