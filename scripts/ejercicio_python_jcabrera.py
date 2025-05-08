def encontrar_caracter (caracter, cadena):
    max_posiciones = len(cadena)
    posiciones = [0] * max_posiciones  # pre-inicializa la lista con ceros
    contador_posiciones = 0

    for p, letra in enumerate(cadena):
        if letra == caracter:
            posiciones[contador_posiciones] = p
            contador_posiciones += 1
            
    resultado_final = posiciones[:contador_posiciones] 
    return resultado_final

caracter_a_buscar = 'a'
texto = 'anana'
resultado = encontrar_caracter (caracter_a_buscar, texto)
print(f"Posiciones de '{caracter_a_buscar}' en '{texto}': {resultado}")