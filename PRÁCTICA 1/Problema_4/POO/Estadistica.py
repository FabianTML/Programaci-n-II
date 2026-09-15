import math

class Estadistica:
    def __init__(self, datos):
        self._datos = list(datos)

    def promedio(self):
        return sum(self._datos) / len(self._datos)

    def desviacion(self):
        n = len(self._datos)
        media = self.promedio()
        suma_cuadrados = sum((x - media) ** 2 for x in self._datos)
        return math.sqrt(suma_cuadrados / (n - 1))