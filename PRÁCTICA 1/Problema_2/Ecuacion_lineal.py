class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def tieneSolucion(self):
        return (self._a * self._d - self._b * self._c) != 0
    def getX(self):
        return (self._e * self._d - self._b * self._f) / \
               (self._a * self._d - self._b * self._c)
    def getY(self):
        return (self._a * self._f - self._e * self._c) / \
               (self._a * self._d - self._b * self._c)