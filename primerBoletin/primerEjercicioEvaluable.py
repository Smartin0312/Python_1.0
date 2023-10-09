numero1=int(input("Dime un numero "))
divisor=int(input("Dime un divisor "))

esDivisible=(numero1%divisor==0)
print(esDivisible)


if numero1%divisor==0:
    esDivisible="Si es divisible "
    

else:
    esDivisible="No es divisible "

print("¿Es el primer número introducido  ",numero1," divisible por el siguiente " ,divisor," ?",esDivisible )
