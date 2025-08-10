"""
3.Usando el concepto de funciones (3 ptos):
Reglas:
- Se requiere verificar una lista de números de diferentes países, el
área de soporte al cliente recibe diariamente ciento de números en
distintos formatos. Estos números pueden venir con o sin código,
espacios, guines, paréntesis, o hasta textos no válido

- Crear la función de normalizar_telefonos(numeros, pais_defecto) la
cual para sus parámetros tendrá las siguientes especificaciones:
numeros: lista con números telefónicos
pais_defecto: en caso no tenga un número un prefijo lo agrega de
acuerdo al país ( “PE”->”+51”, “AR”->”+54”, “CL”->”+56”)
Si el prefijo no existe entre los ya mencionados indicar un mensaje
que no es válido y que debe ingresar un prefijo válido
- Devolverá un dict con:
“válidos”: una lista de números con formato: +<código><numeroNacional>
“invalidos”: lista con los números o valores inválidos y al inicio de esa
lista agregar el valor de “NO VÁLIDOS”
- No mutará la lista de entrada original
"""


# para la revisar enviamos una lista de varios numeros con prefijos y otros datos
nums = [" 987-654321", "(01)234-5678", "+51987654321", "+999123456", "abc"]


def normalizar_telefonos(numeros, pais_defecto):

    # primero definimos los prefijos permitidos
    prefijos = {"PE": "+51", "AR": "+54", "CL": "+56"}

    # si el país no es válido, avisamos y devolvemos listas vacías
    if pais_defecto not in prefijos:
        print("Prefijo no válido. Use PE, AR o CL.")
        return {"válidos": [], "invalidos": ["NO VÁLIDOS"]}

    #definimos las listas para los dicionarios
    validos = []
    invalidos = ["NO VÁLIDOS"]

    #recorremos los numeros ingresados a la funcion
    for numero in numeros:
        # primero limpiamos  dejamos dígitos y un '+' solo si va al inicio
        numero_txt = str(numero)  # convertimos a texto
        limpio = ""
        for caracter in numero_txt:
            if caracter >= "0" and caracter <= "9":
                limpio = limpio + caracter
            elif caracter == "+" and limpio == "":
                limpio = "+"

        # casos de inválidos vacíos
        if limpio == "" or limpio == "+":
            invalidos.append(numero)
            continue

        # en el caso que si ya trae prefijo
        if limpio.startswith("+"):
            if any(limpio.startswith(p) for p in prefijos.values()) and limpio[1:].isdigit():
                validos.append(limpio)
            else:
                # prefijo no válido entre los permitidos
                invalidos.append(f"{numero} - Prefijo no válido. Debe ingresar un prefijo válido")
        else:
            # sin prefijo: agregamos el del país por defecto
            if limpio.isdigit():
                validos.append(prefijos[pais_defecto] + limpio)
            else:
                invalidos.append(numero)

    return {"válidos": validos, "invalidos": invalidos}


print(normalizar_telefonos(nums, "PE"))
