# 2. b) (4,0 valores)
# Desenvolva a função bckSuccess, a criar no módulo Check.py, que deverá retornar uma hashtable
# tendo como chave o host e o valor será uma lista contendo a data e hora em que os backups falharam
# (status != 'Success').

def bckSuccess(backups):
    falhas = {}
    for data, hosts in backups.items():
        for host, horas in hosts.items():
            if host not in falhas:
                falhas[host] = []
            for hora, status in horas.items():
                if status != 'Success':
                    falhas[host].append(f"{data} {hora}")
    return falhas
