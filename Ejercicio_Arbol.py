# Ejercicio 1: Metodo eliminar (un valor)
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo

            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo

            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar(
                nodo.derecho, sucesor.valor
            )

        return nodo


arbol = ArbolBinario()

datos = [50, 30, 70, 20, 40, 60, 80]

for dato in datos:
    arbol.insertar(dato)

print("Árbol antes de eliminar:")
arbol.inorden(arbol.raiz)

print("\n")
arbol.eliminar(50)

print("Árbol después de eliminar 50:")
arbol.inorden(arbol.raiz)
print()


#ejercicio 2: Recorrido por niveles.
from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def recorrido_bfs(self):
        if self.raiz is None:
            return

        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            print(nodo.valor, end=" ")

            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)

            if nodo.derecho is not None:
                cola.append(nodo.derecho)


arbol = ArbolBinario()

datos = [50, 30, 70, 20, 40, 60, 80]

for dato in datos:
    arbol.insertar(dato)

print("Recorrido por niveles (BFS):")
arbol.recorrido_bfs()
print()

# ejercicio 3: sumar todos los valores de un arbol 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)


def sumar_elementos(nodo):
    if nodo is None:
        return 0

    return (
        nodo.valor
        + sumar_elementos(nodo.izquierdo)
        + sumar_elementos(nodo.derecho)
    )


arbol = ArbolBinario()

datos = [50, 30, 70, 20, 40, 60, 80]

for dato in datos:
    arbol.insertar(dato)

total = sumar_elementos(arbol.raiz)

print("Valores del árbol:", datos)
print("La suma de todos los valores es:", total)

# ejercicio 4: Comprobar si cada nodo tiene cero o dos hijos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def es_completo(self, nodo):
        if nodo is None:
            return True

        tiene_izquierdo = nodo.izquierdo is not None
        tiene_derecho = nodo.derecho is not None

        if tiene_izquierdo != tiene_derecho:
            return False

        return (
            self.es_completo(nodo.izquierdo)
            and self.es_completo(nodo.derecho)
        )


arbol = ArbolBinario()

datos = [50, 30, 70, 20, 40, 60, 80]

for dato in datos:
    arbol.insertar(dato)

print("¿El árbol cumple la condición?")
print(arbol.es_completo(arbol.raiz))

otro_arbol = ArbolBinario()

for dato in [50, 30, 20]:
    otro_arbol.insertar(dato)

print("¿El segundo árbol cumple la condición?")
print(otro_arbol.es_completo(otro_arbol.raiz))

# ejercicio 5: Balancear el arbol binario 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)

    def balancear_arbol(self):
        valores = self.obtener_valores()

        def construir(inicio, fin):
            if inicio > fin:
                return None

            medio = (inicio + fin) // 2
            nodo = Nodo(valores[medio])
            nodo.izquierdo = construir(inicio, medio - 1)
            nodo.derecho = construir(medio + 1, fin)
            return nodo

        nuevo_arbol = ArbolBinario()
        nuevo_arbol.raiz = construir(0, len(valores) - 1)
        return nuevo_arbol

    def obtener_valores(self):
        valores = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                valores.append(nodo.valor)
                recorrer(nodo.derecho)

        recorrer(self.raiz)
        return valores

    def por_niveles(self):
        if self.raiz is None:
            return []

        cola = [self.raiz]
        resultado = []

        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.valor)

            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.append(nodo.derecho)

        return resultado


arbol = ArbolBinario()

datos = [10, 20, 30, 40, 50, 60, 70]

for dato in datos:
    arbol.insertar(dato)

print("Árbol original por niveles:")
print(arbol.por_niveles())

balanceado = arbol.balancear_arbol()

print("Árbol balanceado por niveles:")
print(balanceado.por_niveles())

print("Recorrido inorden del árbol balanceado:")
balanceado.inorden(balanceado.raiz)
print()