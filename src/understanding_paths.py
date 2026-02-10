from pathlib import Path 

BASE = Path(__file__).resolve().parent.parent
print(BASE) #Carpeta de mi proyecto

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"

#Creacion de las carpetas
raw.mkdir(parents=True, exist_ok=True)
clean.mkdir(parents=True, exist_ok=True)

#Escribir a un archivo txt
txt_path = raw / "notas.txt"
txt_path.write_text("Mis alumnos favoritos\n Hola chavos\n \t No van a reprobar", encoding="utf-8")
print(contenido)