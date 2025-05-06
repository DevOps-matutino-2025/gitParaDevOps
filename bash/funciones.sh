#!/bin/bash
#

# esta función es lo mismo que el comando basename
fileNameWithoutPath() {   #devuelve el nombre base de un archivo /usr/bin/python --> python
	ruta="$1"
	nombre="${ruta##*/}"
	echo "$nombre"
}

# esta función es lo mismo que el comando dirname
dirNameWithoutFileName() { # ejemplo /usr/bin/python --> /usr/bin
	ruta="$1"
	dir="${ruta%/*}"
	echo "$dir"
}

# esta función hace lo mismo que realpath 
absolutePath() {
	echo "$(cd "$(dirNameWithoutFileName "$1")" && pwd)/$(fileNameWithoutPath "$1")"
}

fileNameWithoutPath "/usr/bin/local/juan.sh"
dirNameWithoutFileName "/usr/bin/local/juan.sh"
absolutePath "../../../../usr/bin/yes"


