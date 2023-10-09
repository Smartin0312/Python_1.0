import random
maquina= random.randint(1,10)
persona=-1
contador=0
while persona!=maquina:
    persona=int(input("dime un numero"))
    contador+=1
    if persona<maquina:
        print("el numero buscado es mas grande ")
    elif persona==maquina:
        print("has acertado en ",contador," intentos")
    else:
        print("El numero es mas bajo")

