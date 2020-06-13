"""
Escribir un programa que pida al usuario dos números enteros y muestre por
 pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números 
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""


dividendo = int (input("escribe un numero que quieras dividir\n"))
divisor = int (input ("escriber el numero por el cual quieres hacer la division\n"))

cociente = dividendo // divisor
resto = dividendo % divisor
print ("el cociente es ", cociente)
print ("y su resto es", resto)

#solucion del autor

"""
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))
"""