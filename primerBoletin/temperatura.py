temperatura=float(input("dime que temperatura tienes"))
encendido=False
if temperatura>=26:
    print("Encendiendo aire acondicionado")
    print("sistema monotorizado adecuadamente")
    encendido=True
    temperatura=float(input("dime que temperatura tienes"))

if encendido==True and temperatura<23:
    print("Apagando aire acondicionado")
if temperatura>=23 and temperatura<=24:
    print("subiendo la temperatura")


print("Registrada"+str(temperatura))
