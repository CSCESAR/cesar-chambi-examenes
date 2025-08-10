"""
2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original

"""
nombres = [
    "  juan perez ",
    "CESAR lopez",
    " Juan Perez",
    " ana  gomez ",
    "MARIA  LOPEZ ",
    "pedro soto"
]

def normalizar_nombres(nombres):
    resultado = []

    #recorremos la lista de nombres
    for nombre in nombres:
        #quitamos espacios antes y después si lo hubiera
        nombre = nombre.lstrip()
        nombre = nombre.rstrip()

        #Convetimo en titulo
        nombre = nombre.title()

        # separamos nombres si hay mas de uno
        nombre = nombre.split()

        #volvemos a unir lo separado
        nombre = " ".join(nombre)

        #armamos nuevamente la lista con valores unicos no duplicados
        if nombre not in resultado:
            resultado.append(nombre)

    return print(resultado)


print(normalizar_nombres(nombres))


