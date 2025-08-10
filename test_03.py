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

def normalizar_telefonos(numeros, pais_defecto):


