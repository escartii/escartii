#!/bin/bash

#Alvaro Escarti :))


# Comprobar si hay actualizaciones disponibles
updates=$(softwareupdate -l)

# Si hay actualizaciones disponibles te las muestra :)
if [ -n "$updates" ]; then
  osascript -e 'display notification "ALVARO ACTUALIZA PERRO!!." with title "Actualizaciones disponibles"'
fi
