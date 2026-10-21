# 2. c) (4,0 valores)
# Considere a criação de uma função AverageBackupTime, a criar no módulo Average.py, que retorne
# a duração média dos registos numa determinada data (e.g. 2024/02/21), utilizando as estruturas de dados já criadas.

def AverageBackupTime(backups, data):
    data_formatada = data.replace('/', '-')
    if data_formatada not in backups:
        return None
    total_segundos = 0
    total_registos = 0
    for host, horas in backups[data_formatada].items():
        for hora in horas.keys():
            partes = hora.split(':')
            segundos = int(partes[0]) * 3600 + int(partes[1]) * 60 + int(partes[2])
            total_segundos += segundos
            total_registos += 1
    if total_registos == 0:
        return None
    media_segundos = int(round(total_segundos / total_registos))
    h = media_segundos // 3600
    m = (media_segundos % 3600) // 60
    s = media_segundos % 60
    return f"{h:02d}:{m:02d}:{s:02d}"
