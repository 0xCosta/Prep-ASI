# 3. b) (3,0 valores)
# Desenvolva a função Control, no módulo Stats.py, que retorne o serviço cujo tempo médio de
# duração das sessões é maior, utilizando a estrutura de dados carregada na alínea anterior.

def Control(res):
    medias = {}
    for servico, datas in res.items():
        duracoes = [u[1] for data in datas.values() for u in data.values()]
        if duracoes:
            medias[servico] = sum(duracoes) / len(duracoes)
    return max(medias, key=medias.get)

def MenorMedia(res):
    medias = {}
    todas_duracoes = []
    for servico, datas in res.items():
        duracoes = [u[1] for data in datas.values() for u in data.values()]
        if duracoes:
            medias[servico] = sum(duracoes) / len(duracoes)
            todas_duracoes.extend(duracoes)
    if not todas_duracoes:
        return []
    media_global = sum(todas_duracoes) / len(todas_duracoes)
    return [servico for servico, media in medias.items() if media < media_global]
