def lugar_c_en_s(c, s)
posiciones = []
for i in range(len(s)):
    if s[i] == c:
        posiciones.append(i)
return posiciones
caracter = input("Ingrese el caracter a buscar: ")
cadena = input("ingrese el sctring donde buscar:")

if len(caracter) !=1:
    print("Error: Debe ingresar solo un caracter")
else:
    resultado = ligar_c_en_s(caracter, cadena)
    printf(f"El caracter ´{caracter}' aparece en las posiciones: {resultado}")
