#!/bin/bash

#Alvaro Escarti

#creo un array para los usuarios
usuarios=(piccolo clarinet horn trunk fiddle viola cello doublebass battery xylophone conductor)

#creo un array para grupos
grupos=(strings woodwind metalwind percussion conductor orchestra)

for crearUsuarios in ${usuarios[@]}; do
    useradd $crearUsuarios &> /dev/null
    grupo=$(id $crearUsuarios | cut -d "=" -f2 | cut -d ")" -f1 | cut -d "(" -f2)
    for i in $grupo; do
	cortargrupos=$(id $crearUsuarios | cut -d "=" -f4)
	echo "el usuario: "$i "pertenece al grupo : "$cortargrupos
    done

done

for crearGrupos in ${grupos[@]}; do
    groupadd $crearGrupos &> /dev/null

done

usermod -aG orchestra piccolo
usermod -aG woodwind piccolo
usermod -aG orchestra clarinet
usermod -aG woodwind clarinet
usermod -aG orchestra horn
usermod -aG metalwind horn
usermod -aG orchestra trunk
usermod -aG metalwind trunk
usermod -aG orchestra fiddle
usermod -aG strings fiddle
usermod -aG orchestra viola
usermod -aG strings viola
usermod -aG orchestra cello
usermod -aG strings cello
usermod -aG orchestra doublebass
usermod -aG strings doublebass
usermod -aG orchestra battery
usermod -aG percussion battery
usermod -aG orchestra xylophone
usermod -aG percussion xylophone
usermod -aG orchestra conductor
usermod -aG conductor conductor
