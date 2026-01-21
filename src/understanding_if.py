user_age = int(input("Ingresa tu edad: "))

if user_age < 0:
    print("Edad invalida")
elif user_age < 18:
    print("Eres menor de edad")
elif 10 <= user_age < 60 and user_age >= 18:
    print("Eres un adulto")
elif 60 <= user_age > 60:
    print("estas casi muerto")