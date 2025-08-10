"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):

Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir un diccionario donde las claves serán
los nombres de los estudiantes y sus valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante y el valor sea otro diccionario con:
promedio: que será el promedio de notas estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio

"""
estudiantes = {
    "Cesar Chambi":[15,16,19],
    "Juan Lopez": [10,8,11],
    "María Jimenez":[16,7,11]
}

def procesar_notas(estudiantes):

    #definimos las variable vacias
    estudiantes_promedio = {}
    mejor_nombre = ""
    mejor_promedio = 0

    #primero recorremos el diccionario
    for estudiante in estudiantes:

        #Motramos las notas
        notas = estudiantes[estudiante]

        #calculamos el promedio con redondeo a un digito
        promedio = round(sum(notas) / len(notas),1)
        #print(f"{estudiante}: {promedio}")

        #determinamos el estado
        if promedio >= 0 and promedio < 11:
            estado = "desaprobado"
        elif promedio >= 11 and promedio <= 20:
            estado = "aprobado"
        else:
            estado = "promedio no válido"
        #print(f"{estudiante}: {estado}")

        #Armamos el nuevo diccionario
        estudiantes_promedio[estudiante] = {"promedio": promedio, "estado": estado}
        #print(estudiantes_promedio)

        #Calculamos el mejor promedio
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_nombre = estudiante
            #print(f"Mejor promedio: {mejor_promedio}: {mejor_nombre}")


    return print(f"El estudiante con mejor proemdio es {mejor_nombre} con un promedio de {mejor_promedio}")

print(procesar_notas(estudiantes))