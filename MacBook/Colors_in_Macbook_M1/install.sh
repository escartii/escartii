#!/bin/bash

#Alvaro Escarti :))

#Poner colores en el editor de texto <nano> de MacOS [ Chip M1 y M2 ]
#Antes que nada, instalar homebrew para instalar el editor nano
brew install nano
#Despues, actualizamos nuestro fichero nanorc
echo 'include "/opt/homebrew/Cellar/nano/*/share/nano/*.nanorc"' >> ~/.nanorc

#Reiniciamos la terminal y ya tenemos los colores :)
