# Programa para obtener estadísticas dada una lista de listas
# La libreria operator con el método itemgetter nos servirá para obtener datos de una lista de listas
import operator


def obtener_estadisticas(lista):  # Función principal para filtrar datos de la lista de listas
    nombres = []
    edades = []
    a = int(0)
    for i in lista:
        nombres.append(operator.itemgetter(0)(lista[a]))  # Separando la lista de listas en dos listas diferentes
        edades.append(operator.itemgetter(1)(lista[a]))
        a += 1
    unique_names = []
    for i in nombres:
        if i not in unique_names:  # Haciendo lista con nombres únicos
            unique_names.append(i)
    sorted_edades = sorted(edades)
    sorted_nombres = sorted(nombres)  # Ordenando nombres y edades
    edad_minima = sorted_edades[0]
    edad_maxima = sorted_edades[len(sorted_edades)-1]  # Asignando resultados
    cantidad_nombres_unicos = len(unique_names)
    nombre_comun = sorted_nombres[0]
    return edad_maxima, edad_minima, cantidad_nombres_unicos, nombre_comun


lista = (("Sofia", 20), ("Adrain", 19), ("Rafael", 20), ("Iris", 19), ("Adrain", 17), ("Adrain", 18))
resultados_estadística = obtener_estadisticas(lista)

print("El rango de edad del grupo es de entre: ", resultados_estadística[0], " y ", resultados_estadística[1], " años")
print("La cantidad de nombres únicos: ", resultados_estadística[2])
print("El nombre más común es: ", resultados_estadística[3])