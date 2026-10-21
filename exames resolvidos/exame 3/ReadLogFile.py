# 2. a) (4,0 valores)
# Ler para hashtables o conteúdo válido (considerando as linhas bem formadas) do ficheiro executando a função
# Read no módulo ReadLogFile.py
# OBS: a hashtable Log deve ter como chave o Host e o valor será uma hashtable com a Data como chave e o valor
# deverá ser uma lista de tuplos contendo o Método, Recurso, HTTP Status e Bytes.

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

def Read(filename="acessos_servidor.txt"):
    Log = {}
    with open(filename, mode='r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            match = padrao_linha.match(linha)
            if not match:
                continue
            dados = match.groupdict()
            host = dados['host']
            data = dados['data']
            metodo = dados['metodo']
            recurso = dados['recurso']
            status = int(dados['status'])
            nbytes = int(dados['bytes'])
            if host not in Log:
                Log[host] = {}
            if data not in Log[host]:
                Log[host][data] = []
            Log[host][data].append((metodo, recurso, status, nbytes))
    return Log
