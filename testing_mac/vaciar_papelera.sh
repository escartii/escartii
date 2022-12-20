#!/bin/bash

#Alvaro Escarti :))

figlet Borrando Basura...
# Vaciar la papelera
rm -rf ~/.Trash/*

# Vaciar la papelera cada hora
while true; do
  sleep 3600
  rm -rf ~/.Trash/*
done
#Importante : para que este script se ejecute automaticamente al reiniciar tu macbook
#Tenemos que abrir la aplicación Lanzadores y añadir nuestro script

