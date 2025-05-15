def buscarPosiciones(cadena, caracter):
    
    posiciones = []
    
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            posiciones.append(i + 1)
    return posiciones

palabra = input("Ingrese una cadena: ")

letra = input ("Ingrese un caracter: ")

print(buscarPosiciones(palabra, letra))


