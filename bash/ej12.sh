#!/bin/bash
#mastermaccontacto@gmail.com
#chuelmo@gmail.com

#Ejercicio 12: De un archivo pasado como parámetro, reportar un listado con las 10 palabras más usadas y cuantas veces se ha usado cada una de ellas, ordenando la salida en forma decreciente en función de la cantidad de veces que se han usado (comenzando desde la palabra más usada a las menos usada). 

#Verificar que se recibe un parámetro y que éste es un archivo

archivo="$1"

for p in `cat "$archivo"`; do
	echo "${p,,}"
done | sort | uniq -c | sort -nr | head -n 10
