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
			echo "suma"
			;;
		2)
			echo "resta"
			;;
		3)
			echo "división"
			;;
		4)
			echo "multiplicar"
			;;
		5)
			echo "Valor ASCII"
			;;
		6)
			echo "Caracter según ASCII"
			#!/bin/bash

			#Verificacion de argumento
			if [ $# -ne 1 ]; then
				echo "Uso $0 <codigo_ascii>"
				exit 1
			fi

			#Conversion e impresion de caracter
			printf "\\x$(printf '%x' "$1")\n"

		7)
			echo "cifrado"
			;;
		8)
			echo "descifrado"
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

