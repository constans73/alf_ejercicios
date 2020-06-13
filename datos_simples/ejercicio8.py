"""Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario y después muestre en pantalla la suma 
de todos los enteros desde 1 hasta 𝑛. 
La suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente forma:
suma =  n(n+1)/2
"""


numero = int(input ("Escribe un numero entero posiitvo\n"))
for i in range(numero):
	numero = numero + i
print ("La suma de todos sus enteros es ", numero)

#solulcion del autor

numero = int(input("Escribe un numero entero positivo\n"))

suma = numero*(numero+1)/2
print ("La suma de todos sus enteros es", suma)
prueba