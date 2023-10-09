var1=float(input("dime un numero"))
vocal=input("dime una cadena")
vocal=vocal.upper()

match vocal:
    case "A"| "a":
        print("Es la primera vocal")
    case "e"| "E":
        print("Es la primera vocal")
    case "i"| "I":
        print("Es la primera vocal")
    case "o"| "O":
        print("Es la primera vocal")
    case "u"| "U":
        print("Es la primera vocal")
    case 1|2|3|4|5|6|7|8|9|10:
        print("es un numero")
    case _:#funciona como else
        print("no es vocal")