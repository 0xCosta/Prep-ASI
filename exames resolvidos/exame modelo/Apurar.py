# 4. b) (4,0 valores)
# Através da invocação da função “acumulado” a criar no módulo “Apurar.py”,
# calcular (através das estruturas de dados já carregadas) o valor acumulado em coimas
# que cada condutor tem. Mostrar o resultado no ecrã.

def acumulado(Condutores, Veiculos):
    resultado_acumulado = {}
    for carta, matriculas in Condutores.items():
        total_condutor = 0.0
        for matricula in matriculas:
            if matricula in Veiculos:
                for data_infracao, dados_infracao in Veiculos[matricula].items():
                    coima_str = dados_infracao[1]
                    coima_limpa = coima_str.replace('€', '').replace(',', '.').strip()
                    try:
                        total_condutor += float(coima_limpa)
                    except ValueError:
                        pass
        resultado_acumulado[carta] = total_condutor
        print(f"Condutor: {carta} - Total Coimas: {total_condutor:.2f}€")
    return resultado_acumulado
