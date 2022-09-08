#Programa No. 7: Elaborar un programa para resolver una ecuación de primer grado

from ast import Str
from calendar import c
from re import A, X


print("--------------------------------------")
print("-----ecuacion de primer grado---------")
print("-------resolver formula Ax+B=c -----")

#input

A =(input("dijite el valor de A:"))
A=int(A)

B =(input("dijite el valor B:"))
B=int(B)

c=(input("dijite el calor de c:"))
c=int(c)


# processing
if A != 0:
        x = (c-B)/A
        print("la solucion es :"+str(x))
else:
    if  A==0 and B!=0 :
        print("la ecuacion no tiene solucion ")
    else:
        print("La ecuacion tiene infinitas soluciones.")

# finis 1
