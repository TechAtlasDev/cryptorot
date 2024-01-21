import json, os

GL = "\033[96;1m" # Azul agua
BB = "\033[34;1m" # Azul claro
YY = "\033[33;1m" # Amarillo claro
GG = "\033[32;1m" # Verde claro
WW = "\033[0;1m"  # Blanco claro
RR = "\033[31;1m" # Rojo claro
CC = "\033[36;1m" # Cyan claro
B = "\033[34m"    # Azul
Y = "\033[33;1m"  # Amarillo
G = "\033[32m"    # Verde
W = "\033[0;1m"   # Blanco
R = "\033[31m"    # Rojo
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado
FONDO_NEGRO = "\033[33;40m"
FONDO_NEUTRO = "\033[0m"
NOTIFICATION = YY+"["+GG+"+"+YY+"]"+WW+" {}"

RUTA_ARCHIVO = "/".join(os.path.abspath(__file__).split("/")[:-1])

# Creando una funcion para operar con la configuracion
def load_json(ruta=f"{RUTA_ARCHIVO}/config.json"):
    archivo = open(ruta, "r").read()
    return json.loads(archivo)

def save_json(data, ruta=f"{RUTA_ARCHIVO}/config.json"):
    with open(ruta, "w") as archivo:
        json.dump(data, archivo, indent=4)


# Creando la función de cifrado
def rot(texto:str, clave:int, cifrar:bool = True, json_return:bool = False):
    """Función de cifrado y descifrado basado en la rotación
    ---
    Esta función permite cifrar un texto basándome en un cifrado de rotación, lo cual, admite los siguientes parámetros:
    - texto (str): Es el texto que se busca modificar.
    - clave (int): Es la cantidad de rotaciones que se busca hacer.
    - cifrar (bool): Identifica si se requiere cifrar o descifrar, siendo True para cifrar y False para descifrar."""

    abecedario = "abcdefghijklmnopqrstuvwxyz"
    texto_cifrado = ""

    for letra in texto:
        puesto = abecedario.find(letra.lower())
        if puesto == -1:
            texto_cifrado += letra
            continue
        else:
            if cifrar:
                puesto_cifrado = puesto+clave
            else:
                puesto_cifrado = puesto-clave

            puestos = puesto_cifrado % len(abecedario)
            lf = abecedario[puestos]
        if letra == letra.upper():
            lf = abecedario[puestos].upper()

        texto_cifrado += lf
    
    if json_return:
        texto_cifrado = {
            "text": texto_cifrado,
            "key": clave
        }

        texto_cifrado = json.dumps(texto_cifrado, indent=4)

    return texto_cifrado