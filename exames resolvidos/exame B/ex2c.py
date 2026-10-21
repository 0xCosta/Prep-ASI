# 2. c) (2,0 valores)
# Através da função AvarageMethod a criar no módulo Average.py retornar o método (e.g. POST, GET, PUT, etc.)
# mais comum num determinado mês, utilizando as estruturas de dados já criadas.

def AvarageMethod(Log, mes):
    mes_str = f"{int(mes):02d}" if str(mes).isdigit() else str(mes).split('-')[-1]
    contagem = {}
    for host, datas in Log.items():
        for data, pedidos in datas.items():
            if data.split('-')[1] == mes_str:
                for pedido in pedidos:
                    metodo = pedido[0]
                    contagem[metodo] = contagem.get(metodo, 0) + 1
    if not contagem:
        return None
    return max(contagem, key=contagem.get)
