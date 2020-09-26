import os
import time


# Función para actualizar la posición del @
def actualizar_pos():
    global dirección
    global pos
    global espacios
    if dirección == "d":
        if pos < espacios:
            pos += 1
            return pos
        else:
            print("No hay más espacios!")
            return pos
    if dirección == "i":
        if pos > 1:
            pos -= 1
            return pos
        else:
            print("No hay mas espacios!")
            return pos
    if dirección == "s":
        print("Hasta luego")
        time.sleep(2)
        exit()


# Función para actualizar el @ si se cumplen las condiciones
def update_chain():
    global dirección
    global symbol
    global espacios
    global pos
    if dirección == "d" and pos < espacios:
        symbol = " " + symbol
        return symbol
    elif dirección == "i" and pos > 1:
        symbol = symbol[1::]
        return symbol
    else:
        return symbol


symbol = "@"
pos = 1
espacios = int(input("Ingresa el número de espacios para mover la figura: "))
os.system("cls")
print(symbol)
while True:
    dirección = (input("Ingresa la dirección para mover la figura d, i, s | Derecha, izquierda, salir: "))
    os.system("cls")
    update_chain()
    actualizar_pos()
    print(symbol)
