# 4. a) (4,0 valores)
# Ler para hashtables o conteúdo do ficheiro dados.txt, invocando e executando
# para o efeito a função “ler” a criar no módulo “Leitura.py”.
# OBS: A hashtable Condutores deverá ter como chave o número da carta de condução e o valor
# será uma lista de veículos/matrículas que essa pessoa tem registados.
# A hashtable Veiculos deverá ter como chave a Matrícula e o valor será uma hashtable com as
# contra ordenações registadas na qual a chave é a data e o valor é uma lista com contra_ordenação,
# coima e data_pagamento_coima).

def ler(ficheiro="dados.txt"):
    Condutores = {}
    Veiculos = {}
    with open(ficheiro, mode='r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            campos = linha.split(';')
            if len(campos) >= 5:
                carta = campos[0].strip()
                matricula = campos[1].strip()
                data = campos[2].strip()
                contra_ordenacao = campos[3].strip()
                coima = campos[4].strip()
                data_pagamento = campos[5].strip() if len(campos) > 5 else ""
                
                if carta not in Condutores:
                    Condutores[carta] = []
                if matricula not in Condutores[carta]:
                    Condutores[carta].append(matricula)
                
                if matricula not in Veiculos:
                    Veiculos[matricula] = {}
                Veiculos[matricula][data] = [contra_ordenacao, coima, data_pagamento]
    return Condutores, Veiculos
