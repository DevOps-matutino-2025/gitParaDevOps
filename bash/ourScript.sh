#!/bin/bash
#
#Cada uno de los alumnos tendrá que resolver un ejercicio dentro de 
#este mismo archivo.
#Luego de resolver los conflictos que encuentren en local, hacer un push de la rama y solicitar un PR
#Cada PR tendrá revisores
#La tarea finalizará cuando el PR quede aprobado
#
#Máximo: corregirá el menú para que llame a cada una de las funciones
#Rodrigo: función sumar()
#Anthony: función restar()
#Joaquín Escudero: función dividir()
#Ignacio: función multiplicar()
#Alvaro: función char2ASCII()
#Giuliana: función ASCII2char()
#Joaquín Manzanar: función cifrar()
#Joaquín Cabrera: función descifrar()

resta(){
	read -p "Ingrese el primer numero: " num1
	read -p "Ingrese el segundo numero: " num2
	resultado=$((num1 - num2))
	echo "El resultado de la resta es: $resultado"
}

while true; do
	clear
	echo "============== MENÚ PRINCIPAL ================"
	echo "1) Sumar 2 números"
	echo "2) Restar 2 números"
	echo "3) Dividir 2 números"
	echo "4) Multiplicar 2 números"
	echo "5) Valor ASCII de un caracter"
	echo "6) Caracter ASCII según un número"
	echo "7) Cifrado de una palabra"
	echo "8) Descifrado de una palabra"
	echo "9) Salir"
	echo "================="
	read -p "Seleccione una opción [1-9]: " opcion

	case $opcion in
		1)
			suma
			;;
		2)

			resta
			;;
		3)
			división
			;;
		4)
			multiplicar
			;;
		5)
			Valor ASCII
			;;
		6)
			Caracter según ASCII
			;;
		7)
			cifrado
			;;
		8)
			descifrado
			;;
		9)
			echo "Saliendo del programa..."
			break
			;;
		*)
			echo "Opción Inválida"
			;;
	esac
	echo ""
	read -p "Presione Enter para continuar..."
done

