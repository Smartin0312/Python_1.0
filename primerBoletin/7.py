var1=float(input("dime un numero"))
var2=float(input("dime otro numero"))
if var1>=0 and var2>=0:
    print("ambos numeros son positivos")
    print("2 positivos")
elif var1<0 and var2<0:
    print("ambos son negativos")
    print("0 positivos")
elif var1<0 and var2>=0:
    print(var1,"es negativo ",var2," es positivo")
    print("1 positivos")
else:
    print(var1," es positivo ",var2," es negativo")
    print("1 positivos")