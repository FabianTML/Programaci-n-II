import time
class Cronometro:
    def __init__(self):
        #inicia con la hora actual
        self._inicia = self._hora_actual_ms()
        self._finaliza = self._inicia
    @staticmethod
    def _hora_actual_ms():
        # da la hora actual en milisegundos
        return int(time.time() * 1000)
    
    def inicia(self):
        self._inicia = self._hora_actual_ms()
    def detener(self):
        self._finaliza = self._hora_actual_ms()
    def getInicia(self):
        return self._inicia
    def getFinaliza(self):
        return self._finaliza
    def lapsoDeTiempo(self):
        return self._finaliza - self._inicia 