from pathlib import Path

class FileManager:
    # Clase base para el manejo de archivos de texto y binarios
    
    def leer_archivo(self, ruta, binario=False):
        # Convertimos la ruta de texto a un objeto Path
        archivo_path = Path(ruta)
        
        # Verificamos si de verdad es un archivo y si existe
        if archivo_path.is_file() == False:
            raise Exception("Error: La ruta que pusiste no existe o no es un archivo válido.")
        
        # Decidimos cómo abrir el archivo usando un if 
        if binario == True:
            modo = 'rb'
        else:
            modo = 'r'
            
        # Abrimos el archivo, lo leemos y devolvemos lo que contiene
        with open(archivo_path, modo) as archivo:
            contenido = archivo.read()
            return contenido

    def escribir_archivo(self, ruta, contenido, binario=False):
        archivo_path = Path(ruta)
        
        # Revisamos si la carpeta donde queremos guardar el archivo existe
        if archivo_path.parent.exists() == False:
            raise Exception("Error: El directorio destino no existe.")
            
        # Elegimos el modo de escritura
        if binario == True:
            modo = 'wb'
        else:
            modo = 'w'
            
        # Abrimos el archivo en modo escritura y guardamos el contenido
        with open(archivo_path, modo) as archivo:
            archivo.write(contenido)