from utils import normalize_name, to_mxn

raw = [
    {"nombre": "     ana     " , "activo": True, "monto": "120.50"},
    {"nombre": "LUIS", "activo": False, "monto": "0"},
    {"nombre": " mara ", "activo": True, "monto": "99.9"} ,

]

def clean(reg):
    return{
        "nombre": normalize_name(reg["nombre"]),
        "activo": bool(reg["activo"]),
        "monto_mxn": to_mxn(reg["monto"], tasa=1.0),

    }

#Lista de diccionarios limpia - clean
clean = [clean(r) for r in raw if r.get("activo")]

print(raw)
print(clean)
