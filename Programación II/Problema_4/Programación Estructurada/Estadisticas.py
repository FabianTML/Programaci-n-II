import math

def leer_numeros(cantidad):
    entrada = input(f"Ingrese {cantidad} números: ")
    valores = entrada.replace(',', ' ').split()
    numeros = [float(v) for v in valores]
    return numeros
def promedio(numeros):
    return sum(numeros) / len(numeros)
def desviacion(numeros):
    n = len(numeros)
    media = promedio(numeros)
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (n - 1))
def main():
    cantidad = 10
    numeros = leer_numeros(cantidad)
    prom = promedio(numeros)
    desv = desviacion(numeros)

    print(f"El promedio es {prom:g}")
    print(f"La desviación estandard es {desv:g}")
    
if __name__ == "__main__":
    main()