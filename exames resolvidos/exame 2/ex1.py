# 1. (5,0 valores)
# Crie um programa em Python que leia um ficheiro e ofusque todas as ocorrências de um número de estudante
# com o formato 8NNNNNN (em que N é um número entre 0 e 9) pelo correspondente valor SHA256, guardando o output
# num ficheiro de saída. Tire partido das expressões regulares para o processo de ofuscação.
# OBS: considere a utilização do módulo hashlib para o hashing do número.

import re
import hashlib

def ofuscar_ficheiro(caminho_entrada, caminho_saida):
    padrao = re.compile(r'\b8[0-9]{6}\b')
    with open(caminho_entrada, mode='r', encoding='utf-8') as f_in:
        conteudo = f_in.read()
    conteudo_ofuscado = padrao.sub(
        lambda m: hashlib.sha256(m.group(0).encode('utf-8')).hexdigest(),
        conteudo
    )
    with open(caminho_saida, mode='w', encoding='utf-8') as f_out:
        f_out.write(conteudo_ofuscado)
