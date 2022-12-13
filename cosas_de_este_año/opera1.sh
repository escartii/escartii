#!/bin/bash

#Alvaro Escarti 

# Crear un array de usuarios
usuarios=(piccolo clarinet horn fiddle viola cello doublebass battery xylophone conductor)

# Crear un array de grupos
grupos=(strings woodwind metalwind percussion conductor orchestra)

for crearUsuarios in ${usuarios[@]}; do
    useradd $crearUsuarios
    groupadd $grupos
done