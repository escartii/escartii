#!/bin/bash

#Alvaro Escarti :))

#Compruebo que el usuario ejecuta el script como sudo
if [ "$EUID" -ne 0 ]; then
    echo "Este script debe ser ejecutado con privilegios de administrador (sudo)."
    exit 1
fi

# Vaciar la papelera en macOS
# Ruta de la papelera en macOS
trash_path="$HOME/.Trash"

# Verificar si la papelera existe y no está vacía
if [ -d "$trash_path" ]; then
    # Vaciar la papelera utilizando el comando "rm"
    sudo rm -rf ~/.Trash/*
    echo "La papelera se ha vaciado correctamente."
else
    echo "La papelera está vacía"
fi

