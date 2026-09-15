import math


class AlgebraVectorial:
    def __init__(self, a=None, b=None):
        self.__a = list(a) if a is not None else [0.0, 0.0]
        self.__b = list(b) if b is not None else [0.0, 0.0]

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def __suma(self, v1, v2):
        return [v1[i] + v2[i] for i in range(len(v1))]

    def __resta(self, v1, v2):
        return [v1[i] - v2[i] for i in range(len(v1))]

    def __magnitud(self, v):
        return math.sqrt(sum(c ** 2 for c in v))

    def __producto_punto(self, v1, v2):
        return sum(v1[i] * v2[i] for i in range(len(v1)))

    def __producto_cruz(self, v1, v2):
        if len(v1) == 2:
            return v1[0] * v2[1] - v1[1] * v2[0]
        return [
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0],
        ]

    def perpendicular(self, criterio="c"):
        a, b = self.__a, self.__b
        if criterio == "a":
            return math.isclose(
                self.__magnitud(self.__suma(a, b)),
                self.__magnitud(self.__resta(a, b)),
                abs_tol=1e-9,
            )
        elif criterio == "b":
            return math.isclose(
                self.__magnitud(self.__resta(a, b)),
                self.__magnitud(self.__resta(b, a)),
                abs_tol=1e-9,
            )
        elif criterio == "c":
            return math.isclose(self.__producto_punto(a, b), 0, abs_tol=1e-9)
        elif criterio == "d":
            suma = self.__suma(a, b)
            return math.isclose(
                self.__magnitud(suma) ** 2,
                self.__magnitud(a) ** 2 + self.__magnitud(b) ** 2,
                abs_tol=1e-9,
            )
        raise ValueError("Criterio no válido, use 'a', 'b', 'c' o 'd'")

    def paralela(self, criterio="f"):
        a, b = self.__a, self.__b
        if criterio == "e":
            razones = []
            for i in range(len(a)):
                if not math.isclose(b[i], 0, abs_tol=1e-9):
                    razones.append(a[i] / b[i])
                elif not math.isclose(a[i], 0, abs_tol=1e-9):
                    return False
            if not razones:
                return True
            return all(math.isclose(r, razones[0], abs_tol=1e-9) for r in razones)
        elif criterio == "f":
            cruz = self.__producto_cruz(a, b)
            if isinstance(cruz, list):
                return all(math.isclose(c, 0, abs_tol=1e-9) for c in cruz)
            return math.isclose(cruz, 0, abs_tol=1e-9)
        raise ValueError("Criterio no válido, use 'e' o 'f'")

    def proyeccion_de_a_sobre_b(self):
        a, b = self.__a, self.__b
        escalar = self.__producto_punto(a, b) / (self.__magnitud(b) ** 2)
        return [escalar * componente for componente in b]

    def componente_de_a_en_b(self):
        a, b = self.__a, self.__b
        return self.__producto_punto(a, b) / self.__magnitud(b)


def main():
    perpendiculares = AlgebraVectorial([1, 0], [0, 1])
    print("Vectores a=(1,0) b=(0,1)")
    print("Perpendicular criterio a:", perpendiculares.perpendicular("a"))
    print("Perpendicular criterio b:", perpendiculares.perpendicular("b"))
    print("Perpendicular criterio c:", perpendiculares.perpendicular("c"))
    print("Perpendicular criterio d:", perpendiculares.perpendicular("d"))

    paralelos = AlgebraVectorial([2, 4], [1, 2])
    print("\nVectores a=(2,4) b=(1,2)")
    print("Paralela criterio e:", paralelos.paralela("e"))
    print("Paralela criterio f:", paralelos.paralela("f"))

    proyeccion = AlgebraVectorial([3, 4], [1, 0])
    print("\nVectores a=(3,4) b=(1,0)")
    print("Proyeccion de a sobre b:", proyeccion.proyeccion_de_a_sobre_b())
    print("Componente de a en b:", proyeccion.componente_de_a_en_b())


if __name__ == "__main__":
    main()
