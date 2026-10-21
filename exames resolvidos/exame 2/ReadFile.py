# 2. a) (4,0 valores)
# Deverá criar e executar a função Read, no módulo ReadFile.py, que permitirá ler para uma estrutura
# hashtables o conteúdo do ficheiro "backup.txt".
# OBS: a hashtable backups deve ter como chave a data no formato AAAA-MM-DD. O valor da hashtable backups será
# uma hashtable com o host como chave e o valor é uma hashtable que tem como chave a hora do backup no formato
# HH:MM:SS e o valor é o status do backup.

def Read(filename="backup.txt"):
    backups = {}
    with open(filename, mode='r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            campos = linha.split(';')
            if len(campos) >= 3:
                data_hora = campos[0].strip()
                host = campos[1].strip()
                status = campos[2].strip()
                partes_dt = data_hora.split(' ')
                data_fmt = partes_dt[0].replace('/', '-')
                hora = partes_dt[1] if len(partes_dt) > 1 else ""
                if data_fmt not in backups:
                    backups[data_fmt] = {}
                if host not in backups[data_fmt]:
                    backups[data_fmt][host] = {}
                backups[data_fmt][host][hora] = status
    return backups
