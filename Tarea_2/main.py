from yaml_manager import YamlManager
# Importamos el decorador 
from schema_validator import schema_validator

# Definimos el esquema 
esquema_personaje = {
    "nombre": str,
    "altura": float,
    "peso": float,
    "edad": int,
    "lista de habilidades": list,
    "descripcion": str
}

# Le ponemos el decorador a nuestra función
@schema_validator(esquema_personaje)
def validar_mis_datos(diccionario_nuevo):
    return diccionario_nuevo

def ejecutar_prueba():
    print("Iniciando la prueba del programa...\n")
    
    # Creamos el objeto de nuestra clase
    manager = YamlManager()
    
    archivo = "datos_proyecto.yaml"
    nombre_diccionario = "mis_registros"

    # Crea un archivo base de texto para empezar
    texto_inicial = "personaje_1:\n  nombre: 'Vacio'\n"
    manager.escribir_archivo(archivo, texto_inicial)
    print("1. Archivo base creado con éxito.")

    # Carga el archivo en la memoria 
    manager.cargar_yaml(nombre_diccionario, archivo)
    print("2. Archivo cargado en la clase YamlManager.")

    # Prepara los datos que queremos guardar
    # Usando datos de prueba 
    datos_estudiante = {
        "nombre": "Andres Chirino",
        "altura": 1.82,
        "peso": 81.0,
        "edad": 21,
        "lista de habilidades": ["Python OOP", "Simulacion en Proteus"],
        "descripcion": "Presidente de Biomecatronica USB"
    }
    
    # Pasamos los datos por la función que tiene el decorador
    datos_revisados = validar_mis_datos(datos_estudiante)
   
    if datos_revisados == None:
        print("\nError: Los datos no cumplen con el esquema.")
        print("Revisa que la edad sea un entero (int), la altura un decimal (float), etc.")
    else:
        print("3. ¡Validación exitosa! Los datos cumplen las reglas.")
        
        # Sacamos el diccionario viejo que ya teníamos guardado
        diccionario_guardado = manager.obtener_diccionario(nombre_diccionario)
        
        diccionario_guardado["personaje_1"] = datos_revisados
        
        # Modificamos la memoria interna y guardamos en el disco duro
        manager.modificar_diccionario(nombre_diccionario, diccionario_guardado)
        manager.guardar_yaml(nombre_diccionario)
        
        print("4. Datos nuevos guardados en el disco correctamente.")
        print(f"\n¡Listo! Abre el archivo '{archivo}' en tu editor de código para ver el resultado final.")

if __name__ == "__main__":
    ejecutar_prueba()