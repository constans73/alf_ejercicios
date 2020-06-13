"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""


inversion = float (input("Introduce la cantidad a invertir\n"))
periodo = int (input("Cuantos años piensas invertirlo\n"))
interes = float (input("a que tipo de interes querrias invertir\n"))

ganancia = inversion * periodo / interes
print ("Con ", inversion, "euros invertido a", periodo, "años y con un tipo de interes de ", interes, "% usted obtendra una ganancia de ", ganancia, "euros")

#solucion del autor


amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
print("Capital final: " + str(round(amount * (interest / 100 + 1) ** years, 2)))
