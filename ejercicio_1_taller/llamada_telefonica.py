# TALLER No.1
# Ejercicio 1 llamada telefonica

from re import L, M, T


print("-----------------------------------")
print("-------COSTO DE LA LLAMDA----------")
print("-----------------------------------")

#input
T = int(input("tiempo de la llamada en minutos:"))

# processing
if T>3:
    mayor=300+50*(T-3)
else: 
    mayor=300

    
#output
print("--------------------------")    
print("----TOTAL A PAGAR---------")
print("--------------------------")
print("el costo de la llamada es:"+str(mayor))
