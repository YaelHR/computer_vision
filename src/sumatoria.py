print(" Este progrsma captura importes")
info = """
            CALCULA TU SUMA
        
        Este programa lleva el conteo de cuentos importes ha 

        """
print(info)
conteo = 0
suma = 0.0
minimo = None 
maximo = None

while True:
    user_message = """
        ingresa tu importe (MXN) 
        sii quieres dejar de capturar importes
        puedes ingresar en cualquier momento
        exit, quit, terminar
        """
        line = input(user_message).lower()
        if line == "exit" or line == "quit" or line == "terminar"
            break
        try:
            value = float(line)
        except ValueError:
            print("Valor invalido, intenta de nuevo")
            continue

        conteo += 1
        suma += value

        if minimo is None or value < minimo:
            minimo = value
        if maximo is None or value > maximo:
        
    if conteo == 0:
        print("no se capturaron importes")
    else:
        print("="*32)
        print("la cantidad de numeros ingresados es: " f"{conteo}")
        print("la sumatorioa de todos los numeros es: " f"{suma}")
        print("El minimo es: "f"{minimo}")
        print("el maximo es: "f"{maxio}")
    
    print("Programa finalizado")












            