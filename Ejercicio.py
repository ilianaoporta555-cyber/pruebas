# Ejercicio 1: Cuenta regresiva
#def countdown(n):
 #   if n == 0:
  #print("¡Despegue!")
   #     return

    #print(n)
    #countdown(n - 1)


#countdown(5)

# Ejercicio 2: invertir una cadena 
#def invertir(cadena):
 #   if cadena == "":
  #      return ""

   # return invertir(cadena[1:]) + cadena[0]


#print(invertir("Recursibidad"))

#Ejercicio 3:Potencia recursiva
#def potencia(a, b):
 #   if b == 0:
  #      return 1
   # return a * potencia(a, b - 1)

#print(potencia(2, 4))  # Salida: 8

#Ejercicio 4: verificar si una palabra es un palíndromo
#def es_palindromo(palabra):
   # if len(palabra) <= 1:
    #    return True
    #if palabra[0] != palabra[-1]:
     #   return False
    #return es_palindromo(palabra[1:-1])

#print(es_palindromo("radar"))  # Salida: True
#print(es_palindromo("python"))  # Salida: False

#ejercicio 5: Encontrar el maximo de una lista
#def encontrar_maximo(lista):
 #   if not lista:
  #      raise ValueError("La lista no puede estar vacía")

   # if len(lista) == 1:
    #    return lista[0]

    #maximo_resto = encontrar_maximo(lista[1:])
    #if lista[0] > maximo_resto:
     #   return lista[0]

   # return maximo_resto


#numero = [3, 5, 2, 8, 1]
#print(encontrar_maximo(numero))  # Salida: 8

#Ejercicio 6: Multiplicacion rusa sin operadaor 

#def multiplicacion_rusa(a, b):
    # Controlar el signo de los números
 #   negativo = (a < 0) != (b < 0)

  #  a = abs(a)
   # b = abs(b)

    #resultado = multiplicar_positivos(a, b)

    #if negativo:
     #   return -resultado

    #return resultado


#def multiplicar_positivos(a, b):
    # Caso base
 #   if b == 0:
  #      return 0

    # Caso recursivo
   # mitad = multiplicar_positivos(a + a, b // 2)

    #if b % 2 == 0:
     #   return mitad

    #return a + mitad


#print(multiplicacion_rusa(5, 4))
#print(multiplicacion_rusa(7, 3))
#print(multiplicacion_rusa(-5, 4))

#Ejercicio 7: Conteo de vocales

#def contar_vocales(texto):
    # Caso base
 #   if texto == "":
  #      return 0

    # Caso recursivo
   # vocales = "aeiouáéíóú"
    #primera = texto[0].lower()

    #if primera in vocales:
     #   return 1 + contar_vocales(texto[1:])

    #return contar_vocales(texto[1:])


#print(contar_vocales("Hola Mundo"))

#Ejercicio 8: Imprimir un patron de asteriscos
#def imprimir_patron(n, nivel=1):
    # Caso base
 #   if nivel > n:
  #      return

    # Imprimir el nivel actual
   # print("*" * nivel)

    # Caso recursivo
    #imprimir_patron(n, nivel + 1)


#imprimir_patron(3)

#Ejercicio 9: Caminos en un tablero 
#def contar_caminos(filas, columnas):
    # Caso base: tablero inválido
 #   if filas <= 0 or columnas <= 0:
  #      return 0

    # Caso base: una sola fila o columna
   # if filas == 1 or columnas == 1:
    #    return 1

    # Caso recursivo: bajar o avanzar a la derecha
    #return (
     #   contar_caminos(filas - 1, columnas)
      #  + contar_caminos(filas, columnas - 1)
    


#print(contar_caminos(3, 3))
#print(contar_caminos(2, 3))

#Ejercicio 10: Aplanar listas anidadas
def aplanar(lista):
    # Caso base
    if lista == []:
        return []

    primero = lista[0]
    resto = lista[1:]

    # Caso recursivo
    if isinstance(primero, list):
        return aplanar(primero) + aplanar(resto)

    return [primero] + aplanar(resto)


datos = [1, [2, [3, 4], 5], 6]

print(aplanar(datos))
