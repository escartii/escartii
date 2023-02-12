# FTP CONFIGURACION


Empezaremos actualizando la maquina
~~~
sudo apt update && sudo apt full-upgrade --yes
~~~
A continuacion instalaremos <code>vsftpd</code> en el servidor
~~~
sudo apt install vsftpd
~~~
En el cliente instalaremos <code>Filezilla</code>
~~~
sudo apt update install filezilla
~~~
Permitir usuarios locales (vsftpd.conf) :
~~~
local_enable=YES
~~~


