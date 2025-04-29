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

descifrar() {
  local texto despl resultado="" car código nuevo

  read -p "Texto cifrado: " texto
  read -p "Desplazamiento (número): " despl

  # Recorremos carácter a carácter
  for (( i=0; i<${#texto}; i++ )); do
    car="${texto:i:1}"
    # Solo letras A–Z y a–z
    if [[ "$car" =~ [A-Z] ]]; then
      código=$(printf '%d' "'$car")
      # A=65…Z=90
      nuevo=$(( (código - 65 - despl + 26) % 26 + 65 ))
      resultado+=$(printf \\$(printf '%03o' "$nuevo"))
    elif [[ "$car" =~ [a-z] ]]; then
      código=$(printf '%d' "'$car")
      # a=97…z=122
      nuevo=$(( (código - 97 - despl + 26) % 26 + 97 ))
      resultado+=$(printf \\$(printf '%03o' "$nuevo"))
    else
      # si no es letra, lo dejamos igual
      resultado+="$car"
    fi
  done

  echo "Texto descifrado: $resultado"
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

