weigth_txt = input("Peso(kg): ")
heigth_txt = input("Altura (m): ")

try:
    weigth = float(weigth_txt)
    heigth = float(heigth_txt)
    imc = weigth / heigth**2
    print(f"Tu IM es {imc}")
except (ValueError, ZeroDivisionError):
    print("Datoa invalidos. Ej. : peso 70.5, altura 1.75")
except  ZeroDivisionError:
    print("Error, no esta permitida la divicion por cero")
except Exception as err:
    print(err)
#print(f"Tu IMC es {imc}")
