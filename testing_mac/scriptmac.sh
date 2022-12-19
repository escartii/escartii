#!/bin/zsh

#Alvaro Escarti :))

#script en el mac
#descubriendo commandos 
saberArquitectura=$(machine)
echo $sberArquitectura
infoFile=$(cksum $1)
#borrarColumnas=$(colrm fichero)
#Informacion sobre tu usuario
#Incluye tu home, nombre personal
# y tambien la shell que utilizas
user=$(last | cut -d " " -f1 | head -n1)
saberStuff=$(pinky -l $user)
echo $saberStuff
echo "Tu arquitectura del procesador es: "$saberArquitectura
echo "El fichero: "$1 "pesa.." $infoFile
#Comando para sacar numeros primos
exit 0

