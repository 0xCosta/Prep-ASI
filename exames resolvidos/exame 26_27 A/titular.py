# 2. a) (1,5 valores)
# Crie um módulo denominado titular.py que contenha uma classe Titular, com os atributos nome e nif.
# A classe deverá incluir um método ofuscar_nif() que devolva o NIF com os seis primeiros algarismos
# substituídos por *, mantendo visíveis os três últimos.
#
# 2. c) (1,0 valor)
# Altere o programa para que a classe Titular inclua um método validar_nif() que verifique se o NIF é
# constituído por exatamente nove algarismos. Apresente o resultado da validação para cada objeto criado.

import re

class Titular:
    def __init__(self, nome, nif):
        self.nome = nome
        self.nif = str(nif)

    def ofuscar_nif(self):
        if len(self.nif) == 9:
            return "******" + self.nif[-3:]
        return self.nif

    def validar_nif(self):
        return bool(re.match(r'^\d{9}$', self.nif))
