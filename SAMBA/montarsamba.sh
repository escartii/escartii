#!/bin/bash

#Alvaro Escarti :))
shared_folder=//server-name/shared-folder

# Definir la ruta de montaje local
mount_point=/mnt/samba

# Crear el punto de montaje si no existe
if [ ! -d $mount_point ]; then
  sudo mkdir $mount_point
fi

# Montar la carpeta compartida
sudo mount -t cifs $shared_folder $mount_point -o username=user,password=pass

# Verificar si el montaje fue exitoso
if [ $? -eq 0 ]; then
  echo "La carpeta compartida se ha montado exitosamente en $mount_point"
else
  echo "Ha ocurrido un error al montar la carpeta compartida."
fi
