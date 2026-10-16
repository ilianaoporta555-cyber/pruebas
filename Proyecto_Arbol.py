# Mini Proyecto: Diccionario Inteligente

class Palabra:
    """Representa una palabra y su definicion."""

    def __init__(self, texto, definicion):
        self.texto = texto.strip().lower()
        self.definicion = definicion

    def __str__(self):
        return f"{self.texto}: {self.definicion}"


class NodoArbol:
    """Nodo del arbol binario de busqueda."""

    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """BST ordenado alfabeticamente por palabra."""

    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = NodoArbol(palabra)
        else:
            self._insertar_rec(self.raiz, palabra)

    def _insertar_rec(self, nodo, palabra):
        if palabra.texto < nodo.palabra.texto:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(palabra)
            else:
                self._insertar_rec(nodo.izquierdo, palabra)

        elif palabra.texto > nodo.palabra.texto:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(palabra)
            else:
                self._insertar_rec(nodo.derecho, palabra)

        else:
            # Actualiza la definicion si la palabra ya existe.
            nodo.palabra.definicion = palabra.definicion

    def buscar(self, texto):
        """Busca una palabra exacta."""
        texto = texto.strip().lower()
        actual = self.raiz

        while actual is not None:
            if texto == actual.palabra.texto:
                return actual.palabra
            elif texto < actual.palabra.texto:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def inorden(self):
        """Retorna las palabras ordenadas alfabeticamente."""
        resultado = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                resultado.append(nodo.palabra)
                recorrer(nodo.derecho)

        recorrer(self.raiz)
        return resultado

    def buscar_por_prefijo(self, prefijo):
        """Retorna las palabras que comienzan con el prefijo."""
        prefijo = prefijo.strip().lower()

        return [
            palabra
            for palabra in self.inorden()
            if palabra.texto.startswith(prefijo)
        ]


# Diccionario inicial: 50 palabras con definiciones.
PALABRAS_INICIALES = [
    ("algoritmo", "Conjunto de pasos para resolver un problema."),
    ("almacenamiento", "Accion de guardar datos o informacion."),
    ("analisis", "Estudio detallado de un tema o problema."),
    ("arbol", "Estructura de datos jerarquica."),
    ("archivo", "Conjunto de datos guardados con un nombre."),
    ("atributo", "Caracteristica que describe un objeto."),
    ("auditoria", "Revision de procesos, datos o controles."),
    ("aurora", "Luz visible en el cielo en ciertas regiones."),
    ("autocompletar", "Funcion que sugiere palabras al escribir."),
    ("autonomia", "Capacidad de actuar con independencia."),
    ("automata", "Modelo abstracto de computacion."),
    ("automatizacion", "Uso de tecnologia para ejecutar tareas."),
    ("base de datos", "Coleccion organizada de informacion."),
    ("binario", "Sistema numerico que usa cero y uno."),
    ("busqueda", "Proceso de localizar un dato."),
    ("byte", "Unidad de informacion digital de ocho bits."),
    ("cadena", "Secuencia de caracteres."),
    ("ciberseguridad", "Proteccion de sistemas y datos digitales."),
    ("ciclo", "Secuencia de pasos que puede repetirse."),
    ("cifrado", "Transformacion de datos para protegerlos."),
    ("codigo", "Instrucciones escritas para una computadora."),
    ("colacion", "Reglas utilizadas para comparar y ordenar texto."),
    ("compilador", "Programa que traduce codigo fuente."),
    ("computadora", "Maquina electronica que procesa informacion."),
    ("condicion", "Expresion que permite tomar una decision."),
    ("contraseña", "Secreto usado para verificar una identidad."),
    ("dato", "Representacion basica de un hecho."),
    ("depuracion", "Proceso de localizar y corregir errores."),
    ("diccionario", "Coleccion de palabras y sus definiciones."),
    ("digital", "Relacionado con datos representados electronicamente."),
    ("estructura", "Forma de organizar elementos."),
    ("funcion", "Bloque reutilizable de codigo."),
    ("hardware", "Componentes fisicos de una computadora."),
    ("informacion", "Datos organizados con significado."),
    ("interfaz", "Medio de interaccion entre usuario y sistema."),
    ("internet", "Red mundial de redes conectadas."),
    ("iteracion", "Repeticion de un proceso o instrucciones."),
    ("lenguaje", "Sistema de simbolos para comunicar instrucciones."),
    ("lista", "Coleccion ordenada de elementos."),
    ("memoria", "Recurso para almacenar datos e instrucciones."),
    ("metodo", "Funcion definida dentro de una clase."),
    ("nodo", "Elemento de una estructura que contiene datos."),
    ("objeto", "Instancia de una clase."),
    ("ordenamiento", "Proceso de organizar elementos segun un criterio."),
    ("palabra", "Unidad del lenguaje con significado."),
    ("programacion", "Actividad de crear instrucciones para un sistema."),
    ("python", "Lenguaje de programacion de alto nivel."),
    ("recursividad", "Tecnica donde una funcion se llama a si misma."),
    ("seguridad", "Proteccion frente a riesgos o accesos no autorizados."),
    ("variable", "Nombre que referencia un valor."),
]


def cargar_diccionario():
    """Construye el BST con las palabras iniciales."""
    arbol = ArbolBinarioBusqueda()

    for texto, definicion in PALABRAS_INICIALES:
        arbol.insertar(Palabra(texto, definicion))

    return arbol


def mostrar_menu():
    print("\n=== DICCIONARIO INTELIGENTE ===")
    print("1. Buscar palabra exacta")
    print("2. Autocompletar por prefijo")
    print("3. Ver diccionario completo")
    print("4. Salir")


def main():
    arbol = cargar_diccionario()
    print(f"Diccionario cargado: {len(arbol.inorden())} palabras.")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            texto = input("Escribe la palabra: ").strip()
            palabra = arbol.buscar(texto)

            if palabra is not None:
                print("\nDefinicion:", palabra.definicion)
            else:
                print("La palabra no esta en el diccionario.")

        elif opcion == "2":
            prefijo = input("Escribe el prefijo: ").strip()

            if not prefijo:
                print("Escribe al menos una letra.")
                continue

            coincidencias = arbol.buscar_por_prefijo(prefijo)

            if coincidencias:
                print("\nSugerencias:")
                for palabra in coincidencias:
                    print("-", palabra.texto)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "3":
            print("\n=== DICCIONARIO EN ORDEN ALFABETICO ===")

            for palabra in arbol.inorden():
                print(palabra)

        elif opcion == "4":
            print("Gracias por utilizar el diccionario.")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    main()