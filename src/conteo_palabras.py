words = "hola hola mundo mundo python mundo datos python hola".split()
print(words)

#Diccionario
freq = {}

for w in words:
    freq[w] = freq.get(w, 0)+1

print(freq)