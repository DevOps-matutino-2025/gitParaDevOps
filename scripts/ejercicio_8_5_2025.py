def lugar_c_enS(c,s):

    lista = []

    for i in range(len(s)):
        if s[i] == c:
            lista.append(i+1)
    return lista

print("Ingrese el string deseado")
frase=input()
print('Ingrese el caracter deseado')
caracter=input()
result=lugar_c_enS(caracter,frase)

print(result)

