#!/bin/bash

# Verificar si el script se está ejecutando como sudo
if [ "$EUID" -ne 0 ]; then
    echo "Este script debe ser ejecutado con privilegios de administrador (sudo)."
    exit 1
fi

# Función para reparar los permisos del sistema
function reparar_permisos() {
    echo "Reparando permisos del sistema..."
    diskutil verifyPermissions /
    echo "Los permisos del sistema han sido reparados."
}

# Función para verificar los archivos de preferencia
function verificar_archivos_preferencia() {
    echo "Verificando archivos de preferencia..."
    find /Library/Preferences -type f -exec plutil -lint {} \;
    echo "La verificación de archivos de preferencia ha finalizado."
}

# Función para realizar una limpieza periódica
function limpieza_periodica() {
    echo "Realizando limpieza periódica..."
    periodic daily weekly monthly
    echo "La limpieza periódica ha sido completada."
}

# Función para limpiar los archivos de caché
function limpiar_cache() {
    echo "Limpiando archivos de caché..."
    rm -rf ~/Library/Caches/*
    echo "Los archivos de caché han sido eliminados."
}

# Función para forzar el vaciado de la Papelera
function forzar_vaciado_papelera() {
    echo "Forzando el vaciado de la Papelera..."
    rm -rf ~/.Trash/*
    echo "La Papelera ha sido vaciada."
}

# Llamar a las funciones según sea necesario
reparar_permisos
verificar_archivos_preferencia
limpieza_periodica
limpiar_cache
forzar_vaciado_papelera

echo "Todas las tareas han sido completadas."

