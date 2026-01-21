def normalize_name(txt):
    """
        Esra funcion normaliza strings,
        Lo que hace es quitar espacios 
        en blanco al inicio y fin de mi
        string, espacios en blanco loz elimina.
        Y el nombre en titulo.
        
        Ej. 
        cArLos    AnToNiO ---> Carlos Antonio

        :params (str): texto de entrada
        :return: texto formateado
    """
    return " ".join(txt.strip().title().split()) #["Carlos" , "Antonio"]

def to_mxn(valor , tasa: float=1.0): #Tasa = parametro opcional
    """
        Convierte valor numerico a MXN multiplicando por la tasa
    """
    return float(valor)*float(tasa)
