import yaml
# Importamos la clase padre del otro archivo
from file_manager import FileManager

class YamlManager(FileManager):
    def __init__(self):
        # Primero llamamos al constructor de la clase padre
        super().__init__()
        self.__data_interna = {}

    def cargar_yaml(self, nombre, ruta):
        # Usamos el método de la clase padre para leer el archivo de texto
        contenido_texto = self.leer_archivo(ruta, binario=False)
        
        # Pasamos los datos a la librería PyYAML para crear el diccionario
        diccionario_yaml = yaml.safe_load(contenido_texto)
        
        # Hacemos una breve validación para que no de error más adelante
        if diccionario_yaml == None:
            diccionario_yaml = {}
            
        # Guardamos todo en nuestro diccionario privado
        self.__data_interna[nombre] = {
            "path": ruta,
            "data": diccionario_yaml
        }

    def obtener_diccionario(self, nombre):
        # Primero verificamos si el nombre existe en nuestro diccionario
        if nombre in self.__data_interna:
            # Si existe, sacamos solo la parte de 'data'
            return self.__data_interna[nombre]["data"]
        else:
            # Si no existe, lanzamos un error
            raise Exception("Error: Ese nombre de diccionario no está guardado.")

    def modificar_diccionario(self, nombre, nuevos_datos):
        # Verificamos que el diccionario exista antes de intentar modificarlo
        if nombre in self.__data_interna:
            # Reemplazamos los datos viejos con los nuevos
            self.__data_interna[nombre]["data"] = nuevos_datos
        else:
            raise Exception("Error: No se puede modificar algo que no existe.")

    def guardar_yaml(self, nombre):
        # Buscamos si tenemos dicho archivo en memoria
        if nombre in self.__data_interna:
            # Sacamos la ruta donde lo vamos a guardar y los datos actualizados
            ruta_para_guardar = self.__data_interna[nombre]["path"]
            datos_para_guardar = self.__data_interna[nombre]["data"]
            
            # Convertimos nuestro diccionario de Python a texto YAML de nuevo
            texto_yaml = yaml.dump(datos_para_guardar, sort_keys=False)
            
            # Usamos el método de la clase padre para escribirlo en el disco
            self.escribir_archivo(ruta_para_guardar, texto_yaml, binario=False)
        else:
            raise Exception("Error: No hay datos guardados con ese nombre para exportar.")