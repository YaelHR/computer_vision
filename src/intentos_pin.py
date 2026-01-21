"""
    Este programam va a pedir al usiario su pin de acceso.
   
    1-si el pin es correcto, entonces el programa debe decirte
    autenticacion exitosa, acceso concedido.

    2- Si el pin ess incorrecto, entonces el programa debe decirle
    pin incorrecto y el numero de intentos de le quedan

    3- Si el usuario suera el numero de intentos permitidos
    entonces el programa le va a decir numero de intentos
    superados y cuenta bloqueada.

    """
    PIN_CORRECTO = "1234"
    INTENTOS_MAX = 3
    intentos = 0

    while intentos < INTENTOS_MAX:
        entrada = input("ingresa tu pin (4 digitos)")
        if entrada ==   PIN_CORRECTO:
            print("autenticacion exitosa")
            print("Acceso concedido")
            break
        else:
            intentos += 1
            restantes = INTENTOS_MAX - intentos
            if restantes >0:
                print("Pin incorercto. Te quedan {restantes} intentos")
            else:
                print("PIN INCORRECTO, CUENTA BLOQUEADA")