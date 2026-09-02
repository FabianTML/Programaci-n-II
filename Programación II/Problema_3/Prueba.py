from Ecuacion_cuadratica import EcuacionCuadratica

def main():
    entrada = input("Ingrese a, b, c: ")
    valores = entrada.replace(',', ' ').split()
    a, b, c = (float(v) for v in valores)
    
    ecuacion = EcuacionCuadratica(a, b, c)
    discriminante = ecuacion.getDiscriminante()
    if discriminante > 0:
        r1 = ecuacion.getRaiz1()
        r2 = ecuacion.getRaiz2()
        print(f"La ecuación tiene dos raíces {r1:g} y {r2:g}")
    elif discriminante == 0:
        # Con discriminante 0, r1 y r2 son iguales (-b / 2a)
        raiz = -b / (2 * a)
        print(f"La ecuación tiene una raíz {raiz:g}")
    else:
        print("La ecuación no tiene raíces reales")

if __name__ == "__main__":
    main()