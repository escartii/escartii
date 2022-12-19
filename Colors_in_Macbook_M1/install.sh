#!/bin/bash

#Alvaro Escarti :))

#Poner colores en la terminal de MacOS [ Chip M1 ]
#Antes que nada, instalar homebrew para instalar el editor nano
brew install nano
#Despues, actualizamos nuestro fichero nanorc
echo 'include "/opt/homebrew/Cellar/nano/*/share/nano/*.nanorc"' >> ~/.nanorc

#Restart ur terminal
