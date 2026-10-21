# 1. (4,0 valores)
# Crie um programa em PYTHON dado um IP em formato CIDR valide se o mesmo esta bem formado.
# (exemplo ip: 192.168.1.0/24; 10.10.10.0/16)

import re

def validar_cidr(ip_cidr):
    padrao = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
        r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
        r'\/(?:3[0-2]|[12]?[0-9])$'
    )
    return bool(padrao.match(ip_cidr.strip()))
