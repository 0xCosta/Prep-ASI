# 2. d) (6,0 valores)
# Tirando partido de expressões regulares, faça um programa em Python para verificar se cada linha do ficheiro está bem formada.
# O formato padrão de cada linha é:
# - Host -> Endereço IPv4 válido: Quatro grupos de números entre 10 e 255, separados por ponto (.). Exemplo válido: 192.168.10.45; Exemplo inválido: 8.8.8.8
# - Data -> Formato AAAA-MM-DD, deve estar entre 2025-01-01 e 2025-12-31 (inclusive). Exemplo válido: 2025-08-15; Exemplo inválido: 2024-02-28
# - Hora -> Formato HH:MM:SS, deve representar uma hora válida entre 00:00:00 e 23:59:59. Exemplo válido: 13:45:02
# - Método -> Um dos seguintes: GET, POST, PUT, DELETE, PATCH. Exemplo válido: POST
# - Recurso -> Deve começar com / e pode conter letras, números, hífens, barras e parâmetros (?, =, &). Exemplo válido: /api/users?id=32; Exemplo inválido: api/users
# - HTTP Status -> Um número de três dígitos, o primeiro dígito deve ser 2, 3 ou 4. Exemplo válido: 200, 302, 404; Exemplo inválido: 500
# - Bytes -> Um número inteiro positivo inferior a 10.000.000. Exemplo válido: 8421; Exemplo inválido: 12500000
# - Separador -> Todos os campos devem ser separados por ";" (ponto e vírgula).

import re

padrao_linha = re.compile(
    r'^(?P<host>(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]));'
    r'(?P<data>2025-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01]));'
    r'(?P<hora>(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]);'
    r'(?P<metodo>GET|POST|PUT|DELETE|PATCH);'
    r'(?P<recurso>\/[a-zA-Z0-9\/\-_?=&\.]*);'
    r'(?P<status>[234][0-9]{2});'
    r'(?P<bytes>[1-9][0-9]{0,6})$'
)

def validar_linha_log(linha):
    return bool(padrao_linha.match(linha.strip()))
