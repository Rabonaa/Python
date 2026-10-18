import math

"""
name = input("Enter your name : ")
age = int(input("Enter your age : "))

print(f'Hello {name}, in 10 years you will be {age + 10} yo.')

"""

"""
print("1. Convertir en Fahrenheit\n"
      "2. Convertir en Celsius\n")
choix = int(input("Saisissez 1 ou 2 : "))

#F = 9/5C + 32

if choix == 1:
    celsius = int(input("Entrer la temperature en degre Celsius : "))
    result = (celsius * 9/5) + 32
    print(result)
else :
    fahrenheit = int(input("Entrer la temperature en degre Fahrenheit : "))
    result = (fahrenheit - 32) * 5/9
    print(result)

"""

"""
rayon = float(input("Entrer le rayon du cercle : "))

aire = math.pi * (rayon**2)
print(f'Aire du cercle : {aire:.2f}')

"""

#a = bq + r

nb = float(input("Saisissez le nombre à diviser : "))
div = float(input("Saisissez le diviseur : "))

print(f'Quotient entier = {nb//div}\n'
      f'Reste = {nb % div}\n'
      f'Resultat en dec = {nb/div}\n')