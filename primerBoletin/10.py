var1=float(input("dime un numero"))
#variable1
if var1%2!=0 and var1%3==0:
    print("es impar y multiplo de 3")
elif var1%2==0 and var1%3==0:
    print(var1," es multiplo de dos y tres ")
    if var1%6==0:
        print("es multiplo de 6")
elif var1%2==0:
    print(var1," es multiplo de dos")
elif var1%3==0:
    print(var1," es multiplo de tres ")
else:
    print("es impar")


