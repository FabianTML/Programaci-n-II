import math


class VectorTridimensional:
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, otro):
        return VectorTridimensional(
            self.a1 + otro.a1, self.a2 + otro.a2, self.a3 + otro.a3
        )

    def __mul__(self, otro):
        if isinstance(otro, VectorTridimensional):
            return self.a1 * otro.a1 + self.a2 * otro.a2 + self.a3 * otro.a3
        return VectorTridimensional(self.a1 * otro, self.a2 * otro, self.a3 * otro)

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __abs__(self):
        return math.sqrt(self.a1 ** 2 + self.a2 ** 2 + self.a3 ** 2)

    def __truediv__(self, escalar):
        return VectorTridimensional(
            self.a1 / escalar, self.a2 / escalar, self.a3 / escalar
        )

    def normal(self):
        return self / abs(self)

    def __xor__(self, otro):
        return VectorTridimensional(
            self.a2 * otro.a3 - self.a3 * otro.a2,
            self.a3 * otro.a1 - self.a1 * otro.a3,
            self.a1 * otro.a2 - self.a2 * otro.a1,
        )

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"

    def __repr__(self):
        return self.__str__()


def main():
    a = VectorTridimensional(1, 2, 3)
    b = VectorTridimensional(4, 5, 6)

    print("a =", a)
    print("b =", b)
    print("a) Suma a + b =", a + b)
    print("b) Escalar 2 * a =", 2 * a)
    print("c) Longitud |a| =", abs(a))
    print("d) Normal de a =", a.normal())
    print("e) Producto escalar a . b =", a * b)
    print("f) Producto vectorial a x b =", a ^ b)


if __name__ == "__main__":
    main()
