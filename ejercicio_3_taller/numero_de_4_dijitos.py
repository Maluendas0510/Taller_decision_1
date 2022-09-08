# ejercicio 2 dterminar si es un numero entero y si es de 4 cifras


print("----------------------------------------")
print("-----NUMERO ENTERO Y DE 4 DIJITOS-------")
print("----------------------------------------")

#otput
N=int(input("dijite el numero:"))

#proceessing
if 1000<=N<=10000:
     print("el numero es de 4 cifras")
else:
    print("el numero no es de 4 cifras")

# finish
 
print("si es entero "+ str(N))