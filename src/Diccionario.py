info_charly = { "name" : "charly" , "age" : "33" , "addres" : "18 O.R." , "salary" : "25,000" , "married" : "True" , 
    
    }
    #imprimir el valor de una llave especifica
print(info_charly["name"])
#imprimr  llaves
print(info_charly.keys())
#imprimir valores
print(info_charly.values())
#imprimir cada llave
for keys,values in info_charly.items():
    print(keys,values)

print(info_charly.get("gender" , ""))