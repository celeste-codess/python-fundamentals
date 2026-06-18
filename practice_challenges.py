#Escribe un programa en Python que pida al usuario ingresar dos números enteros separados por espacio,
#  los convierta a enteros, 
# calcule su suma y muestre el resultado con el mensaje:
#  "La suma es: " seguido del valor.
entrada = input("Ingresa dos números enteros separados por espacio: ")

# 2. Separar el texto por espacios y convertirlos a enteros
datos = entrada.split()
num1 = int(datos[0])
num2 = int(datos[1])

# 3. Calcular la suma
suma = num1 + num2

# 4. Mostrar el resultado con el formato exacto
print(f"La suma es: {suma}")



#Escribe un programa que reciba una lista de números enteros separados por espacios, 
# los almacene en una lista,
#   elimine todos los números pares 
# y luego imprima la lista resultante en una sola línea, 
# con los números separados por espacio.



# 1. Leer la lista de números del usuario y convertirla a enteros
entrada = input("Ingresa los números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

# 2. Filtrar los números para quedarnos solo con los impares (eliminar pares)
impares = [numero for numero in numeros if numero % 2 != 0]

# 3. Imprimir el resultado final FUERA del ciclo en una sola línea
print(*impares, sep=" ")
    


import random
alumnos = ["Ana", "Luis", "Pedro", "Sofía", "Carlos", "Valeria", "Diego", "Mariana"]

def formar_equipos(alumnos):

    equipo1 = []
    equipo2 = []

    for alumno in alumnos:

        elegido = random.choice(alumnos)
        alumnos.remove(elegido)

        if len(equipo1) < 4:
            equipo1.append(elegido)
        else:
            equipo2.append(elegido)

    print("Equipo 1:", equipo1)
    print("Equipo 2:", equipo2)

formar_equipos(alumnos)


#Escribe una función llamada `invertir_numero` 
# que reciba un número entero y devuelva su inverso usando strings.
#  Por ejemplo, si la entrada es 123, la salida debe ser 321. 
# Usa slicing para invertir el número convertido a string.


def invertir_numero(numero):
    a_str = str(numero)
    invertir = a_str[::-1]
    resultado = int(invertir)
    return resultado





#Dada esta lista: letras = ['a', 'b', 'c', 'd', 'e'], 
# escribe un código en Python para recorrerla 
# y crear una nueva lista que contenga todos los elementos
#  excepto las letras 'b' y 'd'.

letras = ['a', 'b', 'c', 'd', 'e']
nuevas_letras=[]

for letra in letras:
    if letra not in ['b', 'd']:
        nuevas_letras.append(letra)
print(nuevas_letras)


mi_tupla = (10, 20, 30)
print(mi_tupla[1])


#Escribe un programa que reciba una palabra y que imprima cada letra en una línea,
#  excepto que si la letra es 'a' debe saltarse (no imprimirse).
#  Usa un ciclo for para recorrer la palabra 
# y la instrucción continue para omitir las letras 'a'.

palabra= input("Dame una palabra: ")
for letra in palabra:
    if letra == "a":
        continue
    print(letra) 



#Escribe un programa que lea una lista de números enteros separados por espacios,
#  luego use un ciclo for para calcular la suma de todos los números
#  pares en esa lista 
# y la imprima.

lista = input("Escribe una lista de numeros eparada por espacios: ")
lista = lista.split()

lista_pares = []
for num in lista:
    numero_int = int(num)
    if numero_int % 2 == 0:
        lista_pares.append(numero_int)

suma=0
for numero_int in lista_pares:
    suma = suma + numero_int

print(f"la suma de los numeros paeres es: {suma}")

#Escribe un programa que lea una palabra, 
# la recorra con un ciclo for y imprima sólo las letras
#  que están en posiciones pares (usando índices 0,2,4...),
#  usando slicing o índice dentro del ciclo.

palabra = input("Escribe una palabra: ")

for letra in palabra[::2]:
    print(letra)

#Escribe un programa en Python que pida al usuario un número entero 
# y muestre si ese número es positivo,
#  negativo o cero. 
# Usa condicionales if, elif y else para determinarlo.

""" num = int(input("Ingresa un número entero:"))

if num > 0:
    print("Es positivo.")
if num < 0:
    print("Es negativo.")
if num == 0:
    print("Es cero.")
 """


#Escribe un programa que reciba una lista de números separados por espacios,
#  convierta esos números a enteros, 
# y luego muestre la suma de todos los números pares que estén en la lista.
#  Usa ciclos for y el operador módulo para identificar los pares.

""" lista = input("Escribe una lista de números separados por espacios:")
lista = lista.split()
par = []
for num in lista:
    a_int=int(num)
    if a_int % 2 == 0:
        par.append(a_int)

print(sum(par)) """

""" suma = 0
for a_int in par:
    suma = suma + a_int
print(suma) """

#Escribe un programa que pida una palabra
#  y muestre las letras de la palabra una por una,
#  pero saltándose las vocales (a, e, i, o, u).
#  Usa un ciclo for, condicionales y la instrucción continue para saltar las vocales.

palabra = input("Dame una palabra:")
for letra in palabra:
    if letra in "aeiouAEIOU":
        continue
    print(letra)

palabra = input("Dame una palabra:")
excluidas = ["a","e","i","o","u"]
for letra in palabra:
    if letra.lower() in excluidas:
        continue
    print(letra)



#Escribe un programa en Python que pida al usuario su nombre y su edad,
#  y luego imprima un mensaje que diga: 
# "Hola <nombre>, tienes <edad> años". 
# Asegúrate de convertir la edad a entero y volver a convertirla a cadena para imprimirla correctamente.
""" 
nombre = input("Escribe tu nombre:")
edad = int(input("Escribe tu edad:"))
print(f"Hola <{nombre}>, tienes <{edad}> años")

#Crea un programa en Python que lea un número entero del
#  usuario y determine si es múltiplo de 3, 4
# múltiplo de 5 o ninguno. Imprime "Múltiplo de 3",
#  "Múltiplo de 5" o "Ninguno" según corresponda.
#  Usa condicionales if, elif, else.

" """

#Escribe un programa que reciba una lista de números enteros separados por espacios,
#  los guarde en una lista,
#  y luego imprima solo los números pares en orden,
#  separados por espacio.
#  Usa un ciclo for y una condición para filtrar pares.
       
lista = input("Escribe una lista de números separados por espacios:")
lista = lista.split()

for num in lista:
    num_int = int(num)
    if num_int % 2 == 0:
        print(num_int, end=" ")

lista = input("Escribe una lista de números separados por espacios:")
lista = lista.split()

suma_pares = 0
for num in lista:
    a_int=int(num)
    if a_int % 2 != 0:
        continue
    print(a_int, end=" ")


radio = float(input("ingresar el radio de un círculo"))
pi = 3.1416
area = pi * (radio ** 2)



#Crea un programa que lea varios números enteros separados por espacios en una sola línea, los almacene en una lista, y luego imprima la suma sólo de los números pares. Usa listas, input(), métodos de listas, y un ciclo for con condición.
lista = input("Escribe una lista de números separados por espacios:")
lista = lista.split()
pares = []
suma_pares = 0
for num in lista:
    a_int=int(num)
    if a_int % 2 == 0:
        pares.append(a_int)
print(sum(pares))

""" antes = 0
ralla = 1
despues = 9
for i in range(10):
    linea = "-" * 10
    print(((antes + i) * " - ") + ralla * " x " + (despues - i) * " - ") """

    #hacer un rango, y cuando lo exida cambiarlooooos

#Escribe un programa en Python que pida al usuario el ancho y el alto de un rectángulo (como números enteros),
#  y que luego calcule y muestre el área del rectángulo usando la función print().
#  Asegúrate de convertir las entradas correctamente y mostrar solo el número del área en la salida.


ancho = int(input("El ancho del rectángulo es: "))
alto = int(input("El alto del rectángulo es: "))
area = ancho * alto
print(area)

word = 'programa'
for letra in word:
    if letra == 'a':
        continue 
print(letra, end='')

#Escribe una función en Python llamada invertir_numero que reciba un número entero
#  y devuelva una cadena con el número invertido usando strings y slicing.

def invertir_numero(numero):
    a_str = str(numero)
    invertir = a_str[::-1]
    return(invertir)

#Escribe una función en Python llamada pares_que_sumen
# que reciba una lista de números y un número objetivo
#  y devuelva una lista con las parejas (tuplas) de números que sumen ese valor.
#  Por ejemplo, para lista=[1,2,3,4] y objetivo=5 debería devolver [(1,4),(2,3)].

""" def pares_que_sumen(lista, objetivo):
parejas = []
    
for n1 in lista:
    for n2 in lista:

        if n1 + n2 == objetivo and n1 < n2:
                parejas.append((n1, n2)) """
                


def pares_que_sumen(lista, objetivo):
    parejas = []
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                parejas.append((lista[i], lista[j]))
                
    return parejas

#recorrer lista y eliminar todos los elementos que sean números pares,
#  usando un ciclo while y el método append()
#  para construir una lista nueva con solo los números impares.

while i < len(lista): # Esto controla cuántas veces se repite (5 veces)
    num = lista[i]
    
    if num % 2 != 0:  # ¡ESTO es lo que decide si es impar!
        impares.append(num)
        
    i += 1

numero = 12345 
print('5' in str(numero))

#número entero y verifique si es múltiplo de 3, 5 o ambos. 
# Imprime: - "Múltiplo de 3" si solo es múltiplo de 3, 
# - "Múltiplo de 5" si solo es múltiplo de 5, - 
# "Múltiplo de 3 y 5" si es múltiplo de ambos, - "No es múltiplo de 3 ni 5" 
# en caso contrario.
#  Usa condicionales if, elif, else y operadores lógicos.
num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("Múltiplo de ambos")
elif num % 3 == 0:
    print("Múltiplo de 3")
elif num % 5 == 0:
    print("Múltiplo de 5")
else:
    print("Multiplo de ninguno" )

#Escribe un programa que lea una palabra 
# y muestre cada letra en una línea,
#  excepto las vocales (a, e, i, o, u)
#  que deben omitirse. Usa un ciclo for para recorrer la palabra y
#  una lista para verificar si una letra es vocal.

#Escribe un programa que lea una frase (string)
#  y recorra cada letra usando un ciclo for.
#  Para cada letra, si es una vocal
#  imprímela en mayúscula, 
# si no, imprímela tal cual. Usa un ciclo for, condicionales y string methods.
palabra = input()
vocales = ["a","e","i","o","u","A", "E","I","O","U"]
for letra in palabra:
    if letra in vocales:
        continue

""" #Completa el siguiente código para que con un ciclo while se impriman los números pares entre 2 y 20.
x = 2
while x <= 20:
    if x % 2 == 0 :
        print(x)
    x += 1

x = 1  # Empezamos en el 1
while x <= 20:  # Buscamos llegar hasta el 20
    x += 1  # 1. ¡PRIMERO HACEMOS AVANZAR EL NÚMERO! (x ahora vale 2)

    if x % 2 != 0:  # 2. Si el número es IMPAR...
        continue  # 3. ¡CORRE AL INICIO! Te saltas el print y vas por el siguiente número

    print(x) """
""" for i in range(5, 16):
     print(i) """

 #calcule y muestre la suma de los números del 1 al 100.

""" suma = 0
for i in range(1, 101):
    suma += i
print(suma) """

#Primero creas tu cofre vacío (suma = 0),
#  luego abres la fila con range(1, 101) recordando que no toca el último número,
#  y dentro usas suma += i para que cada soldado i meta su propio valor (1, luego 2, luego 3...)
#  acumulando el gran total, porque si le sumaras solo 1,
#  el cofre solo contaría de uno en uno y terminaría teniendo 100 monedas en lugar de la suma de todas.
 


""" contador = 1
while contador <= 5:  # ¡Cambiamos el hechizo para incluir al 5!
    print(contador)
    contador += 1 """
    
# contador en 1, mintras 1 siempre es menor a 5 y se imprime el numero k que va sacando 1,2,3,4.5 luego suma de 1 en 1
# el truco esta e el <= por imprimir el 5 y como 6 es mayor solo se rompe


#Corrige el siguiente código para que el ciclo for imprima los números del 0 al 5:

#Escribe un ciclo for en Python que sume los números del 1 al 100 y luego imprima el resultado
""" suma = 0
for i in range(1,101):
    suma += i
print(suma) """

""" for i in range(1,6):
  print(i) """
#Escribe un ciclo while en Python que imprima los números pares del 2 al 20.
""" for i in range(1,11):
    print(i) """

#Escribe un pequeño código que cree un diccionario contando cuántas veces aparece cada letra en la palabra "programa".
""" palabra = "programa"
dicc = {}

for letra in palabra:
    dicc[letra] = dicc.get(letra, 0) + 1 """