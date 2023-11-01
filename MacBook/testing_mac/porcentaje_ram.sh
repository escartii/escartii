#!/bin/bash

# Obtener el porcentaje de RAM utilizado
ram_percentage=$(top -l 1 | awk '/PhysMem/ {print $2/$3 * 100}')

# Imprimir el resultado
echo "Porcentaje de RAM utilizado: "$ram_percentage%
