import random
from Cronómetro import Cronometro

def ordenacion_por_seleccion(lista):
    #Ordena una lista de números
    n = len(lista)
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        # en está parte intercambia el elemento actual con el menor encontrado
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista
def main():
    cantidad = 100_000
    print(f"Generando {cantidad} números random...")
    numeros = [random.randint(0, 1_000_000) for _ in range(cantidad)]
    cronometro = Cronometro()  # inicia automáticamente al crearse
    print("Ordenando....")
    cronometro.inicia()  # reinicio antes de ordenar
    ordenacion_por_seleccion(numeros)
    cronometro.detener()
    tiempo_ms = cronometro.lapsoDeTiempo()
    tiempo_seg = tiempo_ms / 1000.0

    print("\nOrdenación completada")
    print(f"Tiempo transcurrido: {tiempo_ms} ms ({tiempo_seg:.3f} segundos)")
    # verificación de que la lista quedo ordenada
    esta_ordenada = all(numeros[i] <= numeros[i + 1] for i in range(len(numeros) - 1))
    print(f"Lista ordenada correctamente?: {esta_ordenada}")
if __name__ == "__main__":
    main()