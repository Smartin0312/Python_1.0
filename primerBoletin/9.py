var1=float(input("dime un numero"))
var2=float(input("dime otro numero"))
var3=float(input("dime otro numero"))
mayor=0
if var1<var2:
    mayor=var2
elif var1>var2:
    mayor=var1
if mayor<var3:
    mayor=var3
else:
    mayor=mayor
print("el numero mayor es",mayor)    