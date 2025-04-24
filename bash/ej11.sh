#!/bin/bash
#genexits@gmai.com
#Ejercicio 11: Verificar la existencia de un usuario pasado como parámetro. Si el usuario existe deberá desplegarse el texto “el usuario existe!!!” por la salida estándar. En caso que el usuario no exista, deberá desplegarse el texto “No existe!!!” por la salida estándar y devolviéndose un 1 como código de retorno del script.

if [ $# -ne 1 ]; then
	echo "USO: $0 <usuario>"
	exit 2
fi

usuario="$1"

#if egrep -q "^$usuario:" /etc/passwd; then
#	echo "El usuario $usuario existe"
#else
#	echo "El usuario $usuario NO existe"
#	exit 1
#fi


#for u in `cut -d: -f1 /etc/passwd`; do
#	if [[ "$u" == "$usuario" ]]; then
#		echo "El usuario $usuario existe"
#		exit 0
#	fi
#done

#echo "El usuario $usuario NO existe"
#exit 1


if id "$usuario" >/dev/null 2>&1; then
	echo "El usuario $usuario existe"
else
	echo "El usuario $usuario NO existe"
	exit 1
fi
	
	
