var1=input("dime un caracter")

if var1=="a"or var1=="A":
    print("Es la primera vocal ")
elif var1=="e"or var1=="E":
    print("Es la segunda vocal ")
elif var1=="i"or var1=="I":
    print("Es la tercera vocal ")
elif var1=="o"or var1=="O":
    print("Es la cuarta vocal ")
elif var1=="u"or var1=="U":
    print("Es la quinta vocal ")
else:
    print("El caracter introducido no es una vocal")     
  
match var1:
    case 1:
        print("es un numero")