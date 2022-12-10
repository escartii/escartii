#!/bin/bash


#Alvaro Escarti

ruta=/srv/mount-point

if [ -d $ruta ]; then
    echo "Los directorios se comparten"
else
    sudo mount 192.168.9.5:/srv/nfs /srv/mount-point/ | logger -s
    sudo mount 192.168.9.5:/srv/nfs/exportados-todos /srv/mount-point | logger -s

fi

exit 0


