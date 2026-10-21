# 2. b) (2,0 valores)
# Desenvolver uma função CheckLogs a criar no módulo Check.py que deve retornar uma lista com os pedidos em
# que o valor dos dados transmitidos ultrapassou os 2048 bytes utilizando as estruturas de dados anteriormente criadas.

def CheckLogs(Log):
    pedidos = []
    for host, datas in Log.items():
        for data, lista_pedidos in datas.items():
            for pedido in lista_pedidos:
                if pedido[3] > 2048:
                    pedidos.append((host, data, pedido[0], pedido[1], pedido[2], pedido[3]))
    return pedidos
