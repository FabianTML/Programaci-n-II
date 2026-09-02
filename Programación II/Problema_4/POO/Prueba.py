from Estadistica import Estadistica

def main():
    cantidad = 10
    entrada = input(f"Ingrese {cantidad} números: ")
    valores = entrada.replace(',', ' ').split()
    numeros = [float(v) for v in valores]
    
    estadistica = Estadistica(numeros)
    print(f"El promedio es {estadistica.promedio():g}")
    print(f"La desviación estandard es {estadistica.desviacion():g}")

if __name__ == "__main__":
    main()