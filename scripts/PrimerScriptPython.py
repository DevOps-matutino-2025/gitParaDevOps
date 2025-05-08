def lugar_c_en_S(c, s):
    lista = []
    cont = 0

    for i in s:
        if i == c:
            lista += [cont]
        cont += 1

    return lista

c = 'a'
s = 'anana'

print(lugar_c_en_S(c, s))



#Maximo Brassetti