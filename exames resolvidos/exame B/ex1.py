# 1. (6,0 valores)
# Crie um programa em Python que leia um ficheiro de texto contendo registos de acessos a um sistema informático.
# Cada linha do ficheiro pode conter:
# - Endereços IP (ex.: 192.168.0.15),
# - Datas no formato YYYY-MM-DD,
# - Nomes de utilizadores (ex.: user_jose, admin_maria, etc.).
# O programa deve:
# - Ofuscar os endereços IP, substituindo os dois primeiros grupos de números por ***, mas mantendo os restantes; Exemplo: 192.168.0.15 -> ***.***.0.15
# - Converter todas as datas para o formato DD/MM/YYYY; Exemplo: 2025-10-24 -> 24/10/2025
# - Anonimizar os nomes de utilizador, substituindo-os por "utilizador_X", onde X é um número incremental (1, 2, 3, ...); Exemplo: user_jose, admin_maria -> utilizador_1, utilizador_2
# - Remover linhas em branco e espaços duplicados do ficheiro.
# - Guardar o resultado num novo ficheiro cujo nome seja o nome original seguido de _anon.txt.

import re

def anonimizar_ficheiro(caminho_ficheiro):
    if caminho_ficheiro.endswith('.txt'):
        caminho_saida = caminho_ficheiro[:-4] + '_anon.txt'
    else:
        caminho_saida = caminho_ficheiro + '_anon.txt'

    padrao_ip = re.compile(r'\b\d{1,3}\.\d{1,3}\.(\d{1,3}\.\d{1,3})\b')
    padrao_data = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')
    padrao_user = re.compile(r'\b(?:user|admin)_[a-zA-Z0-9_]+\b')

    mapa_utilizadores = {}
    contador_utilizador = [1]

    def callback_utilizador(match):
        nome = match.group(0)
        if nome not in mapa_utilizadores:
            mapa_utilizadores[nome] = f"utilizador_{contador_utilizador[0]}"
            contador_utilizador[0] += 1
        return mapa_utilizadores[nome]

    linhas_processadas = []
    with open(caminho_ficheiro, mode='r', encoding='utf-8') as f_in:
        for linha in f_in:
            linha = linha.strip()
            if not linha:
                continue
            linha = re.sub(r' +', ' ', linha)
            linha = padrao_ip.sub(r'***.***.\1', linha)
            linha = padrao_data.sub(r'\3/\2/\1', linha)
            linha = padrao_user.sub(callback_utilizador, linha)
            linhas_processadas.append(linha)

    with open(caminho_saida, mode='w', encoding='utf-8') as f_out:
        for l in linhas_processadas:
            f_out.write(l + '\n')
