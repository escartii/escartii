#!/bin/bash

#ALvaro Escarti :))


if ! [ $# -ne 3 ]; then
    #compruebo que existe un usuario, si existe envio la salida al agujero negro
    if id "$1" >/dev/null 2>&1; then 
    echo "user exists"
    echo "/home/$1"
    if [ $2 = "replenish" ]; then
        echo "Hola"
    fi
else 
    echo "Error - The user given not exists " 
fi
else
    echo "Put 3 arguments"
    exit 1
fi

