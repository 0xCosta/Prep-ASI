# 2. d) (3,0 valores)
# Desenvolver as funções TotalBackups e TotalFailed, a criar no módulo Stats.py, que retornem
# o número de registos realizados e o número de Failed registados, respetivamente, por host.

def TotalBackups(backups):
    totais = {}
    for data, hosts in backups.items():
        for host, horas in hosts.items():
            if host not in totais:
                totais[host] = 0
            totais[host] += len(horas)
    return totais

def TotalFailed(backups):
    falhas = {}
    for data, hosts in backups.items():
        for host, horas in hosts.items():
            if host not in falhas:
                falhas[host] = 0
            for hora, status in horas.items():
                if status == 'Failed':
                    falhas[host] += 1
    return falhas
