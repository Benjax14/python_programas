print("!Bienvenidos!\n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División")

select = input("Seleccione una opción: ")

match select:
    case "1":
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print("La suma es: ",n1+n2)
    case "2":
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print("La resta es: ",n1-n2)
    case "3":
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print("La multiplicación es: ",n1*n2)
    case "4":
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print("La división es: ",n1/n2)
    case _:
        print("Seleccion no valida")
