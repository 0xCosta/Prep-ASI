# 2. (4,0 valores)
# Faça um programa em PYTHON que valide, através de uma expressão regular,
# se uma data e hora introduzida no formato AAAA/MM/DD HH:MM:SS é válida.
# Exemplos:
# 2016/05/15 23:43:01 -> Válido
# 2016/05/15 24:00:59 -> Inválido
# 2015/13/21 12:00:01 -> Inválido

import re

def validar_data_hora(data_hora_str):
    padrao = re.compile(
        r'^\d{4}\/(?:0[1-9]|1[0-2])\/(?:0[1-9]|[12]\d|3[01])\s(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$'
    )
    return bool(padrao.match(data_hora_str.strip()))
