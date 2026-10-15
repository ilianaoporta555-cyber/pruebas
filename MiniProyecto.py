#Mini Proyecto: Explorador de Directorios 

class ExploradorRecursivo:
    """Explorador recursivo de un sistema de archivos."""

    @staticmethod
    def imprimir_arbol(sistema, nivel=0):
        """
        Imprime carpetas y archivos con indentacion.

        Caso base: el diccionario esta vacio.
        Caso recursivo: recorrer cada carpeta anidada.
        """
        if not sistema:
            return

        for nombre, contenido in sistema.items():
            espacios = "    " * nivel

            if isinstance(contenido, dict):
                print(f"{espacios}[CARPETA] {nombre}/")

                # Llamada recursiva para entrar en la carpeta
                ExploradorRecursivo.imprimir_arbol(
                    contenido, nivel + 1
                )
            else:
                print(f"{espacios}[ARCHIVO] {nombre} ({contenido})")

    @staticmethod
    def buscar_archivo(sistema, nombre, ruta=""):
        """
        Busca un archivo y devuelve su ruta completa.

        Caso base: encuentra el archivo o termina de recorrer
        el diccionario sin encontrarlo.
        Caso recursivo: entra en cada subcarpeta.
        """
        for nombre_actual, contenido in sistema.items():
            if ruta:
                nueva_ruta = f"{ruta}/{nombre_actual}"
            else:
                nueva_ruta = nombre_actual

            if isinstance(contenido, dict):
                resultado = ExploradorRecursivo.buscar_archivo(
                    contenido, nombre, nueva_ruta
                )

                if resultado is not None:
                    return resultado

            elif nombre_actual == nombre:
                return nueva_ruta

        # Caso base: el archivo no existe en esta rama
        return None

    @staticmethod
    def contar_archivos(sistema):
        """
        Cuenta todos los archivos, sin contar las carpetas.

        Caso base: diccionario vacio, devuelve cero.
        Caso recursivo: suma los archivos y los de las
        subcarpetas.
        """
        total = 0

        for contenido in sistema.values():
            if isinstance(contenido, dict):
                total += ExploradorRecursivo.contar_archivos(
                    contenido
                )
            else:
                total += 1

        return total


# Estructura de ejemplo del sistema de archivos
sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}


# 1. Imprimir el arbol de directorios
print("=== ARBOL DE DIRECTORIOS ===")
ExploradorRecursivo.imprimir_arbol(sistema_archivos)

# 2. Buscar un archivo
print("\n=== BUSQUEDA DE ARCHIVO ===")
archivo = ExploradorRecursivo.buscar_archivo(
    sistema_archivos, "perro.jpg"
)

if archivo is not None:
    print(f"Archivo encontrado: {archivo}")
else:
    print("Archivo no encontrado")

# 3. Contar los archivos
print("\n=== TOTAL DE ARCHIVOS ===")
total = ExploradorRecursivo.contar_archivos(
    sistema_archivos
)
print(f"Cantidad total de archivos: {total}")