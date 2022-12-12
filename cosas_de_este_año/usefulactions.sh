#!/bin/bash

#ALvaro Escarti :))
usuario=$1

if ! [ $# -ne 3 ]; then
    #compruebo que existe un usuario, si existe envio la salida al agujero negro
    if id "$1" >/dev/null 2>&1; then 
    echo "user exists"
    echo "/home/$1"
    if [ $2 = "replenish" ]; then
        # Creo un array con los nombres de los directorios que quieres crear
        cd $HOME/$usuario
        mkdir $HOME/$usuario/SolarSystem
        directorios=(dir1 dir2 dir3)
        for directorio in ${directorios[@]}; do
            mkdir $directorio
        done
    fi
else 
    echo "Error - The user given not exists " 
fi
else
    echo "Put 3 arguments"
    exit 1
fi

