import os
import time
palabra = "@"
espacios = int(input("Ingresa el número de espacios para mover la figura: "))
pos = 1
while True:
    os.system("cls")
    print(palabra)
    dirección = input("Ingresa la dirección para mover la figura d, i, s | Derecha, izquierda, salir: ")
    if dirección == "d":
        if pos <= espacios:
            palabra = " " + palabra
            pos += 1
        else:
            print("¡No se puede continuar!")
            time.sleep(1)
    elif dirección == "i":
        if pos > 1:
            pos += -1
            palabra = palabra[1::]
        elif pos <= 1:
            print("¡No se puede continuar!")
            time.sleep(1)
    elif dirección == "s":
        break