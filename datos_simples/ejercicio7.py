"""Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""


horas = float (input ("¿Cuantas horas has trabajado?\n"))
valor = float (input ("¿Cual es el valor de las horas?\n"))

resultado = horas * valor

print ("La paga que te coresponde es de ",resultado," euros")


#solucion del autor


"""
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))
"""