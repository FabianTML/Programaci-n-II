import math


class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distancia(self, arg1, arg2=None):
        if isinstance(arg1, MiPunto):
            otro_x = arg1.get_x()
            otro_y = arg1.get_y()
        else:
            otro_x = arg1
            otro_y = arg2
        return math.sqrt((self.__x - otro_x) ** 2 + (self.__y - otro_y) ** 2)


def main():
    p1 = MiPunto()
    p2 = MiPunto(10, 30.5)
    print(f"p1 = ({p1.get_x()}, {p1.get_y()})")
    print(f"p2 = ({p2.get_x()}, {p2.get_y()})")
    print(f"Distancia entre p1 y p2: {p1.distancia(p2)}")
    print(f"Distancia entre p1 y (10, 30.5): {p1.distancia(10, 30.5)}")


if __name__ == "__main__":
    main()
