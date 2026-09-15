from Ecuacion_lineal import EcuacionLineal

def main():
    entrada = input("Ingrese a, b, c, d, e, f: ")
    valores = entrada.replace(',', ' ').split()
    
    a, b, c, d, e, f = (float(v) for v in valores)
    ecuacion = EcuacionLineal(a, b, c, d, e, f)
    if ecuacion.tieneSolucion():
        x = ecuacion.getX()
        y = ecuacion.getY()
        print(f"x = {x}, y = {y}")
    else:
        print("La ecuación no tiene solución")

if __name__ == "__main__":
    main()