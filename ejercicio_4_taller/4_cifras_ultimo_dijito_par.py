#Programa No. 4: Construir un programa que lea un número entero y que determine si su último dígito es un número par.

import math


print("--------------------------------------------")
print("---numero de 4 cifras y su ultimo dijito:---")
print("--------------------------------------------")

#input
n=input("Digite un numero entero :")
n=int(n)

#processing
if n%2 == 0:
    print("ultimo dijito es par")
else:
    print("ultimo dijito no es par")