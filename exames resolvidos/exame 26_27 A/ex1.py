# 1. (4,0 valores)
# Crie um programa em Python que leia um ficheiro de texto e ofusque todas as ocorrências de números de
# identificação fiscal portugueses, constituídos por nove algarismos consecutivos, guardando o resultado num
# ficheiro de saída em que sejam visíveis apenas os últimos três algarismos de cada número, substituindo os
# restantes por *.
# Exemplo:
# • Entrada: O NIF do cliente é 245123678.
# • Saída: O NIF do cliente é ******678.
# O programa deverá preservar todo o conteúdo do ficheiro original que não corresponda a números de
# identificação fiscal e utilizar expressões regulares para identificar os números a ofuscar.

import re

def ofuscar_nifs(caminho_entrada, caminho_saida):
    padrao = re.compile(r'\b\d{6}(\d{3})\b')
    with open(caminho_entrada, mode='r', encoding='utf-8') as f_in:
        conteudo = f_in.read()
    conteudo_ofuscado = padrao.sub(r'******\1', conteudo)
    with open(caminho_saida, mode='w', encoding='utf-8') as f_out:
        f_out.write(conteudo_ofuscado)
