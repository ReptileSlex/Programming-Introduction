fila_a = ["a", "b", "c", "d", "e", "f", "g"]
fila_b = ["u", "v", "w", "x"]
fila_combinada = []


def combinar_filas(fila_a, fila_b):
    a = 0
    b = len(fila_b)
    for persona in fila_b:
        fila_combinada.append(fila_a[a])
        fila_combinada.append(fila_b[a])
        a += 1
    for persona in range(0, b-1):
        fila_combinada.append(fila_a[b])
        b += 1
    return fila_combinada


print(fila_a)
print(fila_b)
combinar_filas(fila_a, fila_b)
print(fila_combinada)