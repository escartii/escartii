#!/bin/bash

#Alvaro Escarti :))


# Comprobar si hay actualizaciones disponibles
updates=$(softwareupdate -l)

# Si hay actualizaciones disponibles te las muestra :)
if [ -n "$updates" ]; then
  osascript -e 'display notification "Hay actualizaciones disponibles para tu sistema." with title "Actualizaciones disponibles"'
fi
