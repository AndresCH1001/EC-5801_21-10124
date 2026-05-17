import math
from typing import List

# Representa un punto en el espacio
class Punto:
    def __init__(self, x: float, y: float, z: float):
        # Atributos privados 
        self.__x: float = x
        self.__y: float = y
        self.__z: float = z

    # Funciones GETTER para que otras clases puedan leer las coordenadas
    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_z(self) -> float:
        return self.__z

    # Metodo para sumar un valor a todos los ejes
    def sumar_escalar(self, valor: float) -> None:
        self.__x += valor
        self.__y += valor
        self.__z += valor

    # Metodo para multiplicar ejes especificos
    def multiplicar_escalar(self, valor: float, ejes: List[str]) -> None:
        if "x" in ejes: self.__x *= valor
        if "y" in ejes: self.__y *= valor
        if "z" in ejes: self.__z *= valor

# Hereda de Punto
class Vector(Punto):
    def __init__(self, x: float, y: float, z: float):
        # Usamos super() para inicializar la clase padre
        super().__init__(x, y, z)

    # Metodo para calcular la magnitud (norma) del vector
    def calcular_magnitud(self) -> float:
        # Usamos los getters porque no tenemos acceso directo a __x, __y, __z
        x = self.get_x()
        y = self.get_y()
        z = self.get_z()
        
        # Formula matematica: raiz de la suma de los cuadrados
        return math.sqrt(x**2 + y**2 + z**2)

# Prueba
if __name__ == "__main__":
    # Creamos un vector
    v1 = Vector(2.0, 2.0, 2.0)
    print(f"Coordenadas iniciales: X={v1.get_x()}, Y={v1.get_y()}, Z={v1.get_z()}")
    print(f"Magnitud: {v1.calcular_magnitud()}")

    # Operacion de suma escalar
    v1.sumar_escalar(5.0)
    print(f"\nDespues de sumar 5 a todo: X={v1.get_x()}")
    print(f"Nueva magnitud: {v1.calcular_magnitud():.2f}")