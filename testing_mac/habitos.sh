#!/bin/bash

# Enviar una notificación
osascript -e 'display notification "¡No olvides beber agua!" with title "Recordatorio de agua"'

# Establecer un temporizador para que el script se ejecute cada 2 horas
while true; do
  sleep 7200
  osascript -e 'display notification "¡No olvides beber agua!" with title "Recordatorio de agua"'
done
