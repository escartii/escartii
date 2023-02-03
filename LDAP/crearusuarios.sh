#!/bin/bash

#Alvaro Escarti :))

touch ldapusers.ldif
fichero="ldapusers.ldif"


#Crear usuarios con fichero ldif y despues añadiremos con lmodify -x -D 
for i in $(seq 5 99); do
	echo "dn: uid=mkt$i,ou=Marketing,dc=tkj,dc=cloud" >> $fichero
	echo "ObjectClass: inetOrgPerson" >> $fichero
	echo "ObjectClass: posixAccount" >> $fichero
	echo "ObjectClass: top" >> $fichero
	echo "cn: marketing$i" >> $fichero
	echo "sn: mkt$i" >> $fichero
	echo "uidNumber: 10$i" >> $fichero
	echo "gidNumber: 10000" >> $fichero
	echo "homeDirectory: /home/mkt$i" >> $fichero
	echo "loginShell: /bin/bash"
	echo "usersPasswords: PATATON" >> $fichero
	echo "" >> $fichero

done

exit 0
