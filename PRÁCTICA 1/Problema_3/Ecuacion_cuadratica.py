import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def getDiscriminante(self):
        #Retorna el discriminante
        return self._b ** 2 - 4 * self._a * self._c
    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self._b + math.sqrt(discriminante)) / (2 * self._a)
    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self._b - math.sqrt(discriminante)) / (2 * self._a)