#!/bin/zsh

#Alvaro Escarti :))

echo "Mostrar el procesador de tu MacBook, no importa si es intel o ARM..."

mostrarCPU=$(sysctl -n machdep.cpu.brand_string)
echo $mostrarCPU


#hola
exit 0
