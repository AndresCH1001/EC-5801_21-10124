import time
from typing import List, Union

# --- MODELADO DE HARDWARE ---

class DiscoDuro:
    def __init__(self, n: int):
        self.memoria: List[int] = [0] * n
        self.retardo: float = 0.1  # Muy lento (100ms)

    def leer(self, posicion: int) -> int:
        time.sleep(self.retardo)
        return self.memoria[posicion]

    def escribir(self, posicion: int, dato: int) -> None:
        time.sleep(self.retardo)
        self.memoria[posicion] = dato

class MemoriaRAM:
    def __init__(self, n: int):
        self.memoria: List[int] = [0] * n
        self.retardo: float = 0.01  # Lento (10ms)

    def leer(self, posicion: int) -> int:
        time.sleep(self.retardo)
        return self.memoria[posicion]

    def escribir(self, posicion: int, dato: int) -> None:
        time.sleep(self.retardo)
        self.memoria[posicion] = dato

class MemoriaSRAM:
    def __init__(self, n: int):
        self.memoria: List[int] = [0] * n
        self.retardo: float = 0.001  # Muy rapido (1ms)

    def leer(self, posicion: int) -> int:
        time.sleep(self.retardo)
        return self.memoria[posicion]

    def escribir(self, posicion: int, dato: int) -> None:
        time.sleep(self.retardo)
        self.memoria[posicion] = dato

# --- FUNCIONES POLIMORFICAS (BUS DE MEMORIA) ---

# Union permite que el bus acepte cualquiera de las tres clases
TipoMemoria = Union[DiscoDuro, MemoriaRAM, MemoriaSRAM]

def bus_lectura(dispositivo: TipoMemoria, posicion: int) -> int:
    """Funcion polimorfica que lee sin importar el tipo de hardware"""
    print(f"Accediendo a {type(dispositivo).__name__}...")
    return dispositivo.leer(posicion)

def bus_escritura(dispositivo: TipoMemoria, posicion: int, dato: int) -> None:
    """Funcion polimorfica que escribe sin importar el tipo de hardware"""
    print(f"Escribiendo en {type(dispositivo).__name__}...")
    dispositivo.escribir(posicion, dato)

# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    # Inicializamos los componentes
    hd = DiscoDuro(120)
    ram = MemoriaRAM(102)
    sram = MemoriaSRAM(1022)

    # Probamos la escritura polimorfica
    bus_escritura(hd, 0, 1000)
    bus_escritura(ram, 0, 2000)
    bus_escritura(sram, 0, 3000)

    # Probamos la lectura polimorfica
    valor = bus_lectura(ram, 0)
    print(f"Valor leido de RAM: {valor}")