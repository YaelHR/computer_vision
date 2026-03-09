#Determina si un año del calendario gregoriano es bisiesto.
year = int(input("ingresa el año: "))
if year < 1582 or year > 9999:
    print("El año no es valido")

if year % 400 == 0:
        print("True")
    elif year % 100 == 0:
        print("False")
    elif year % 4 == 0:
        print("True")
    else:
        print("False")






























