#!/bin/bash

#Alvaro Escarti =))
#2 SMX

echo "el script que esta ejecutando el script es: "$USER

if [ $USER = "trasgos" ]; then
	exit 0
else
	echo " [** LETS CREATE PATH FOR NFS... **]"
	mkdir -p /srv/nfs/exam-ldap-nfs
	servidor=192.168.5.126
	punto_montaje=/srv/nfs/exam-ldap-nfs
	recurso=/$servidor/compartido
	mount $servidor:$recurso $punto_montaje

	if [ $? -eq 0 ]; then
	    echo "el servidor NFS se ha montado en: " $punto_montaje
	else
	    echo "No se puede montar el servidor NFS en: $punto_montaje"
	fi
fi

exit 0
