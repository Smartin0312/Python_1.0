import random
var1=0
var1=input("dime piedra |papel |tijera")
maquina=random.randint(0,2)
print("Apuesta de la maquina",maquina)
print("Apuesta del jugador",var1)
var1=int(input("dime un numero del 1-3"))
if maquina==1:
    print