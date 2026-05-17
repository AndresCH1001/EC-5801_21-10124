from typing import List

class Matriz:
    def __init__(self, n_columnas: int, m_filas: int):
     
        self.n: int = n_columnas
        self.m: int = m_filas

        self.datos: List[List[float]] = [[0.0 for _ in range(n_columnas)] for _ in range(m_filas)]

    def imprimir(self) -> None:
        # Recorremos cada fila de la matriz
        for fila in self.datos:
            # 8 espacios de ancho y 2 decimales
            fila_texto = " ".join(f"{valor:>6.2f}" for valor in fila)
            # Imprimimos la fila con bordes
            print(f"| {fila_texto} |")

    # Operacion de Suma (+)
    def __add__(self, otra: 'Matriz') -> 'Matriz':
        # Las matrices deben tener el mismo tamaño
        if self.m != otra.m or self.n != otra.n:
            raise ValueError("Las dimensiones deben ser iguales para sumar")
        
        # Creamos una matriz nueva para el resultado
        resultado = Matriz(self.n, self.m)
        
        # Recorremos filas y columnas para sumar posicion por posicion
        for i in range(self.m):
            for j in range(self.n):
                resultado.datos[i][j] = self.datos[i][j] + otra.datos[i][j]
        
        return resultado

    # Operacion de Resta (-)
    def __sub__(self, otra: 'Matriz') -> 'Matriz':
        # Las matrices deben tener el mismo tamaño
        if self.m != otra.m or self.n != otra.n:
            raise ValueError("Las dimensiones deben ser iguales para restar")
        
        # Creamos una matriz nuevamente para el resultado
        resultado = Matriz(self.n, self.m)
        
        # Recorremos filas y columnas para restar posicion por posicion
        for i in range(self.m):
            for j in range(self.n):
                resultado.datos[i][j] = self.datos[i][j] - otra.datos[i][j]
        
        return resultado 
    # Operacion de Multiplicacion (*)
    def __mul__(self, otra: 'Matriz') -> 'Matriz':
        # Columnas de A (self.n) deben ser igual a Filas de B (otra.m)
        if self.n != otra.m:
            raise ValueError("Las columnas de la primera matriz deben coincidir con las filas de la segunda")

        # La matriz resultante sera de tamaño: Filas de A (self.m) x Columnas de B (otra.n)
        resultado = Matriz(otra.n, self.m)

        # Triple bucle para el producto punto
        for i in range(self.m):           # Recorre las filas de la primera matriz
            for j in range(otra.n):       # Recorre las columnas de la segunda matriz
                for k in range(self.n):   # Realiza la sumatoria de los productos
                    resultado.datos[i][j] += self.datos[i][k] * otra.datos[k][j]
        
        return resultado

    # Deshabilitar Operacion de Division (/)
    def __truediv__(self, otra: 'Matriz'):
        # Lanzamos un error
        raise TypeError("La division de matrices no esta definida")  
    
    def cargar_datos(self, lista_valores: List[List[float]]) -> None:
        """Metodo sencillo para llenar la matriz con datos de prueba"""
        if len(lista_valores) == self.m and len(lista_valores[0]) == self.n:
            self.datos = lista_valores
        else:
            raise ValueError("La lista de valores no coincide con el tamaño N x M")      
    
    # Prueba
if __name__ == "__main__":
    # Definimos las dimensiones de las matrices
    A = Matriz(2, 2)
    B = Matriz(2, 2)

    # Cargamos los datos
    A.cargar_datos([[120, 20], 
                    [30, 40]])
    
    B.cargar_datos([[52, 51], 
                    [521, 51]])

    # Colocamos la operación
    resultado = A * B

    # Mostramos el resultado
    print("Resultado:")
    resultado.imprimir()