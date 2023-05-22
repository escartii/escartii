#!/bin/bash

# Verificar si el comando figlet está instalado
if ! command -v figlet &> /dev/null; then
    echo "El comando figlet no está instalado. Instálalo antes de ejecutar este script."
    exit 1
fi

# Función para mostrar un mensaje en arte ASCII generado por figlet
function mostrar_mensaje_figlet() {
    local mensaje=$1

    # Verificar si el mensaje no está vacío
    if [[ -n $mensaje ]]; then
        figlet "$mensaje"
    else
        echo "No se ha proporcionado ningún mensaje para mostrar."
    fi
}

# Ejemplo de uso del comando figlet en el script
mostrar_mensaje_figlet "COMANDOS GIT"

echo " "
echo "------------------"
echo " "
echo "git add -> añadir los cambios sobre el fichero modificado"
echo " "
echo "git commit -> añadir un comentario sobre los cambios realizados"
echo " "
echo "git push origin main -> subir los cambios a tu rama main"
echo " "
echo "git pull -> traigo mis cambios en mi repositorio remoto"
echo " "
