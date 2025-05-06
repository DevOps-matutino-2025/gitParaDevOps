#!/bin/bash
#Vamos a ver como hacer una pila (stack) con un array y procesar ese stack
#hasta que no quede ningún elemento.
#En el stack vamos a poner algunos colores y los vamos a ir imprimiendo por pantalla y sacando del stack, si en el stack encontramos la palabra primario o secundario sacaremos esa palabra del stack y agregaremos los colores correspondientes que están en los arrays primarios y secundarios.
#Además si encontramos la palabra oscuro agregaremos al stack el color "negro"

primarios=("rojo" "amarillo" "azul")
secundarios=("naranja" "verde" "morado")
stack=("rosa" "oscuro" "blanco" "primario" "marrón" "gris" "secundario")

while [[ ${#stack[@]} -gt 0 ]]; do #Mientas el array tenga elementos

	color="${stack[-1]}" #Cargamos en color el último elemento del stack

	if [ "$color" == "primario" ]; then
		unset 'stack[-1]'
		stack+=("${primarios[@]}") #Expansión de array para agregar todos los elementos al stack
	elif [ "$color" == "secundario" ]; then
		unset 'stack[-1]'
		stack+=("${secundarios[@]}")
	elif [ "$color" == "oscuro" ]; then
		unset 'stack[-1]'
		stack+=("negro")
	else
		echo "$color"
		unset 'stack[-1]' #Eliminamos el último elemento del stack
	fi
done
