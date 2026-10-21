# 3. a) (5,0 valores)
# Implemente a função Ler, no módulo LerFicheiro.py, que leia o conteúdo do ficheiro e armazene os
# registos numa estrutura de dados baseada em dicionários (hashtables).
# O dicionário res deverá ter como chave o serviço e como valor um dicionário cuja chave é a data. Para cada data,
# o valor deverá ser outro dicionário com a chave 'utilizador' e o valor correspondente a um tuplo com o tempo de
# autenticação e a duração da sessão, ambos convertidos para segundos.

def tempo_para_segundos(hms):
    partes = hms.split(':')
    return int(partes[0]) * 3600 + int(partes[1]) * 60 + int(partes[2])

def Ler(ficheiro="acessos.txt"):
    res = {}
    with open(ficheiro, mode='r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            campos = linha.split(';')
            if len(campos) >= 5:
                utilizador = campos[0].strip()
                servico = campos[1].strip()
                t_auth = tempo_para_segundos(campos[2].strip())
                duracao = tempo_para_segundos(campos[3].strip())
                data = campos[4].strip()
                
                if servico not in res:
                    res[servico] = {}
                if data not in res[servico]:
                    res[servico][data] = {}
                res[servico][data][utilizador] = (t_auth, duracao)
    return res
