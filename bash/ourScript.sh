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

division() {
    echo "Ingrese el dividendo"
	read -r num1
	echo "Ingrese el divisor"
	read -r num2

	# Verifica que ambos parámetros sean números (enteros o decimales)

	es_numero='^-?[0-9]+([.][0-9]+)?$'

	if ! [[ $num1 =~ $es_numero ]]; then
	  echo "Error: '$num1' no es un número válido."
	  exit 2
	fi

	if ! [[ $num2 =~ $es_numero ]]; then
 		echo "Error: '$num2' no es un número válido."
  		exit 2
	fi

	#Verificacion del divisor
	if [[ $(echo "$num1 == 0" | bc) -eq 1 ]]; then
  		echo "Error: División por cero"
  		exit 3
	fi

	result=$(echo "scale=2; $num1 / $num2" | bc)

	echo "Resultado: $result"
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
			;;
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

