
# Variables
# 1. Inicializa una variable entera y muestra su valor
variable = 5
print((variable))
# Esperado: 5

# 2. Inicializa una variable de punto flotante y muestra su valor
flotante = 3.14
print(flotante)  # Esperado: 3.14

# 3. Inicializa una cadena y muestra su longitud
nombre = "Python"
print(len(nombre))  # Esperado: 6

# 4. Inicializa una lista y muestra su primer elemento
lista = [1, 2, 3]
print(lista[0])  # Esperado: 1

# 5. Inicializa un diccionario y muestra un valor por clave
diccionario = {'a': 1, 'b': 2}
print(diccionario['a'])  # Esperado: 1

# Condicionales
# 6. Comprobar si un número es par
num = 4
if num % 2 == 0:
    print("Es par")  # Esperado: "Es par"

# 7. Verificar si una cadena contiene una subcadena
cadena = "Hola Mundo"
if "Mundo" in cadena:
    print("Contiene 'Mundo'")  # Esperado: "Contiene 'Mundo'"

# 8. Clasificar un número como positivo, negativo o cero
num = -1
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")  # Esperado: "Negativo"
else:
    print("Cero")

# 9. Comprobar si un año es bisiesto
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Bisiesto")  # Esperado: "Bisiesto"
# 10. Validar un número de rango
num = 15
if num < 1 or num > 10:
    print("Fuera de rango")

# 11. Imprimir números del 1 al 5 usando un bucle for
print(", ".join(str(i) for i in range(1, 6)))

# 12. Sumar los primeros 10 números naturales
suma = sum(range(1, 11))
print(suma)

# 13. Crear una lista con los cuadrados de los primeros 5 números
cuadrados = [i**2 for i in range(1, 6)]
print(cuadrados)

# 14. Contar cuántas vocales hay en una cadena
cadena = "Hola"
vocales = sum(1 for char in cadena if char.lower() in 'aeiou')
print(vocales)

# 15. Imprimir una tabla de multiplicar del 3
tabla_3 = [3 * i for i in range(1, 11)]
print(", ".join(str(num) for num in tabla_3))

# Esperado: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

# 16. Colecciones
lista = []
lista.append(1)
print(lista)  # Esperado: [1]
lista.append(2)
print(lista)  # Esperado: [1, 2]


#EJERCICIO 17
conjunto = {1, 2, 3}
print(1 in conjunto) 

#EJERCICIO 18
diccionario = {}
diccionario['a'] = 1
print(diccionario) 

#EJERCICIO 19
lista = [3, 1, 2]
lista.sort()
print(lista)  

#EJERCICIO 20
lista = [1, 2, 3]
print(len(lista))  

#EJERCICIO 21
lista = [1, 2, 3, 4, 5]
print(sum(lista)) 

#EJERCICIO 22
lista = [1, 2, 3, 4, 5]
pares = [x for x in lista if x % 2 == 0]
print(pares) 

#EJERCICIO 23
cadena = "Hola Mundo"
print(len(cadena.split()))  

#EJERCICIO 24
lista = [1, 3, 2]
print(max(lista))  

#EJERCICIO 25
lista = [True, True, False]  

#EJERCICIO 26
lista = [False, False, True]
print(any(lista)) 

#EJERCICIO 27
claves = ['a', 'b', 'c']
valores = [1, 2, 3]
diccionario = dict(zip(claves, valores))
print(diccionario) 

#EJERCICIO 28
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
tuplas = list(zip(lista1, lista2))
print(tuplas) 

#EJERCICIO 29
lista = [1, 2, 1, 3]
print(lista.count(1))

#EJERCICIO 30
n = 5
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci[:n])

#EJERCICIO 31
lista = [1, 2, 3]
print(lista[::-1]) 

#EJERCICIO 32
lista1 = [1, 2]
lista2 = [3, 4]
print(lista1 + lista2) 

#EJERCICIO 33
import random
numeros_aleatorios = [random.randint(1, 10) for _ in range(5)]
print(numeros_aleatorios) 


############################################################
# 34. Contar la cantidad de elementos en un conjunto
conjunto = {1, 2, 3}
resultado = len(conjunto)
print(resultado)

##########################################################
# 35. Crear un diccionario a partir de una lista de tuplas
tuplas = [(1, 'a'), (2, 'b')]
resultado = dict(tuplas)
print(resultado)  
##########################################################
# 36. Obtener los elementos únicos de una lista
lista = [1, 2, 2, 3]
resultado = list(set(lista))
print(resultado)  
############################################################
# 37. Verificar si un diccionario contiene una clave
diccionario = {'a': 1}
resultado = 'a' in diccionario
print(resultado) 
##############################################################
# 38. Fusionar dos diccionarios
dic1 = {'a': 1}
dic2 = {'b': 2}
resultado = {**dic1, **dic2}
print(resultado) 
##############################################################
# 39. Convertir una lista en un conjunto
lista = [1, 2, 2, 3]
resultado = set(lista)
print(resultado)  
##############################################################
# 40. Obtener los elementos de un diccionario en forma de lista
diccionario = {'a': 1, 'b': 2}
claves = list(diccionario.keys())
valores = list(diccionario.values())
print(claves)  
print(valores)  
##############################################################
# 41. Calcular la suma de los valores en un diccionario
diccionario = {'a': 1, 'b': 2}
resultado = sum(diccionario.values())
print(resultado) 
##############################################################
# 42. Filtrar un diccionario por un valor mínimo
diccionario = {'a': 1, 'b': 2, 'c': 3}
resultado = {k: v for k, v in diccionario.items() if v >= 2}
print(resultado) 
#############################################################
# 43. Crear un contador de palabras
cadena = "Hola mundo hola"
palabras = cadena.split()
resultado = {palabra: palabras.count(palabra) for palabra in set(palabras)}
print(resultado)  
##############################################################
# 44. Obtener los elementos comunes entre dos listas
lista1 = [1, 2, 3]
lista2 = [2, 3, 4]
resultado = list(set(lista1) & set(lista2))
print(resultado)  
##############################################################
# 45. Comprobar si una lista es un subconjunto de otra
lista1 = [1, 2]
lista2 = [1, 2, 3]
resultado = set(lista1).issubset(lista2)
print(resultado)  

# 46. Generar una lista de números pares del 1 al 20
resultado_46 = [x for x in range(1, 21) if x % 2 == 0]
print(resultado_46) 
#############################################################
# 47. Crear un diccionario de frecuencias de una lista
lista = [1, 2, 2, 3]
resultado_47 = {x: lista.count(x) for x in set(lista)}
print(resultado_47)  
###########################################################
# 48. Unir dos listas alternando sus elementos
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado_48 = [elem for pair in zip(lista1, lista2) for elem in pair]
print(resultado_48)  
###############################################################
# 49. Encontrar el índice de un elemento en una lista
lista = [1, 2, 3]
resultado_49 = lista.index(2)
print(f"El valor de 2 es el índice {resultado_49}")  
#########################################################################
# 50. Crear un diccionario a partir de una lista de claves y valores
claves = ['a', 'b']
valores = [1, 2]

diccionario = dict(zip(claves, valores))

print(diccionario)

# 51. Filtrar palabras largas de una lista
palabras = ["uno", "dos", "tres", "cuatro"]
palabras_largas = []
for palabra in palabras:
    if len(palabra) > 4:
        palabras_largas.append(palabra)
print(palabras_largas)

# 52. Crear una lista de los índices de los elementos en una lista
lista = [10, 20, 30]
indices = []
for i in range(len(lista)):
    indices.append(i)
print(indices)

# 53. Ordenar un diccionario por sus valores
diccionario = {'a': 3, 'b': 1, 'c': 2}
ordenado = {}
valores_ordenados = sorted (diccionario.values())
for valor in valores_ordenados:
    for clave in diccionario:
        if diccionario [clave] == valor:
            ordenado[clave] = valor
print(ordenado)

# 54. Verificar si dos listas son iguales
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
son_iguales = True
if len(lista1) != len(lista2):
    son_iguales = False
else:
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            son_iguales = False
            break
print(son_iguales)

# 55. Crear un conjunto a partir de una lista con duplicados
lista = [1, 1, 2, 3]
conjunto = set()
for elemento in lista:
    conjunto.add(elemento)
print(conjunto)

# 56. Calcular el promedio de una lista
lista = [1, 2, 3, 4, 5]
suma = 0
for numero in lista:
    suma += numero
promedio = suma / len(lista)
print(promedio)

# 57. Comprobar si una lista está vacía
lista = []
if len(lista) == 0:
    print(True)
else:
    print(False)

# 58. Obtener los elementos únicos de una lista manteniendo el orden
lista = [1, 2, 2, 3]
unicos = []
for elemento in lista:
    if elemento not in unicos:
        unicos.append(elemento)
print(unicos)

#59. Contar las letras en una cadena
cadena = "Hola"
conteo = {}
for letra in cadena:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1
print(conteo)

# 61. Eliminar un elemento de una lista
lista = [1, 2, 3]
lista.remove(2)
print(lista)

# 62. Repetir una cadena varias veces
cadena = "Hola"
repetida = cadena * 3
print(repetida)

# 63. Crear una lista de números aleatorios y ordenarla
import random
numeros = []
for i in range(10):
    numeros.append(random.randint(1, 100))
numeros.sort()
print(numeros)

# 64. Crear una lista de listas
lista_de_listas = [[1, 2], [3, 4]]
print(lista_de_listas)

#Integrantes 
"""
Hernandez Vega Jairo Noe
Perez Sandoval Diego Antonio 
Mendoza Marin Christian Eduardo
Garzon Rangel Rene
"""