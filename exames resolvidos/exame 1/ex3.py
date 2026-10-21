# 3. (4,0 valores)
# Crie um programa em PYTHON que dada uma string com um nome, telefone (Portugal) e data de
# nascimento valide se os dados estão bem inseridos e indique quantos anos terá a pessoa no ano atual.
# Por exemplo: “Jose Maria Almeida;00351 962341234;1997-12-19” deverá dar como output
# “Nome, Numero de Telemóvel e Data Valida, em 2018 terá 21 anos”. Recorra a expressão regulares para resolver o exercício.

import re
from datetime import date

def validar_pessoa(dados_str):
    padrao = re.compile(
        r'^(?P<nome>[a-zA-ZÀ-ÿ\s]+);'
        r'(?P<telefone>(?:00351|\+351)?\s?[29]\d{8});'
        r'(?P<ano>\d{4})-(?P<mes>0[1-9]|1[0-2])-(?P<dia>0[1-9]|[12]\d|3[01])$'
    )
    match = padrao.match(dados_str.strip())
    if not match:
        return "Dados Invalidos"
    ano_nascimento = int(match.group('ano'))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return f"Nome, Numero de Telemovel e Data Valida, em {ano_atual} tera {idade} anos"
