# Caso 2. intricciones condicionales
# ejercicio No.2 hallar el mayor de tres numeros

print("-------------------------------")
print("------MAYOR DE 3 ENTEROS-------")
print("-------------------------------")

# input
a = int(input("digite el primer numero:"))
b = int(input("digite el segundo numero:"))
c = int(input("digite el tercer numero:"))

# processing
if a>b:
    if a>c:
        mayor=a
    else:
        mayor=c
else:
    if b>c:
        mayor=b
    else:
        mayor=c
        
#output
print("--------------------------")
print("---------RESULTADO--------")
print("--------------------------")
print ( "El mayor entre "  +  str ( a ) +  ", "  +  str ( b ) +  " y "  +  str ( c ) +  " es: "  +  str ( mayor ))
