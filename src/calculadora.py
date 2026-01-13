#Este preograma pide al usuario una cantidad en pesos pexicanos,
#Tambien pide el personaje en iva y el porcentaje de propina
#El programa debe calcular el monto tolal a pagar por el cliente
subtotal = input("subtotal(mxn): ")
iva_txt = input("IVA(%) ej. 16: ")
propina_txt = input("Propina (%) ej. 10: ")

try:
    #Metodo built-in float - convirte a un dato del tipo flotante
    subtotal = float(subtotal_txt)
    iva = float(iva_txt)/100
    propina = float(propina_txt)/100
eexcept ValueError:
    print("Enrada ivalida. Utiliza numeros")

monto_iva = subtotal*iva
monto_propina = subtotal*propina
totsl = subtotal+monto_iva+monto_propina

print(f"Subtotal: {subtotal}")
print(f"IVA: {monto_iva}")
print(f"Propina: {monto_propina}")
print(f"Total:{total}")