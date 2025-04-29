# grupoDevOps

## Buenas prácticas
Siempre trabajo en local.

Para trabajar me creo mi propia rama (los nombres de las ramas dependen de la cultura organizacional)

Antes de hacer un push, actualizo la branch desde la cual yo estoy trabajando, soluciono los conflictos y hago el merge en local y luego si puedo hacer el push.

## Nombres de los integrantes

Joaquin Escudero 

Maximo Brassetti

Giuliana Pedemonti 

Christian Huelmo

Rodrigo Camaño

# Introducción

- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## Ejercicios
1. Verificar que se tiene el repo actualizado
2. Cada estudiante crea su rama con el nombre rama_nroEstudiante
3. Crear el archivo estudiantes.txt
4. Escribir en una línea el correo electrónico
5. Esperar a que el profesor también cree su rama y la mergee con main
6. Hacer el merge con main resolviendo los conflictos que encuentre
    * Me cambio a main y hago un pull (actualizo en local main)
    * Vuelvo a cambiar a mi rama
    * git merge main (me puede dar o no conflictos)
    * soluciono los conflictos, hago el merge y luego que el merge es exitoso
    * hago el push
8. Actualizar el repo remoto

### Parte II - Buenas prácticas
1. Crear la rama feature/bash
2. Crear la carpeta bash
3. Moverse a la carpeta bash
4. Agregar los 2 ejercicios de la rama scripts
5. Agregarle a cada uno un comentario en la segunda línea con el correo
6. Hacer el commit
7. Actualizar main
8. Hacer el merge desde la rama feature/bash con main
9. Resolver los problemas en local, charla de buenas prácticas

### Parte III - Conquistando los puntos
1. En local moverse y actualizar la rama main
2. Modificar el archivo estudiantes agregándole su nombre
3. Hacer el commit correspondiente
4. Hacer el push en la rama main
5. Enviar una captura de pantalla al correo del profesor, asunto: nombre del alumnos - captura push en main
6. Revertir el último commit
7. Enviar captura de pantalla al correo del profesor, asunto: nombre del alumno - revert del commit
8. Crear la rama feature/NombreAlumno
9. Modificar el script ourScript.sh que se encuentra en la carpeta bash
10. Resolver conflictos en local
11. Hacer el push de la rama
12. Solicitar un PR de lo subido
