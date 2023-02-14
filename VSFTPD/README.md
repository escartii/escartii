# FTP CONFIGURACION


Empezaremos actualizando la maquina
~~~
sudo apt update && sudo apt full-upgrade --yes
~~~
instalaremos <code>Filezilla</code>
~~~
sudo apt update install filezilla
~~~

A continuacion instalaremos <code>vsftpd</code> en el servidor
~~~
sudo apt install vsftpd
~~~
Ahora creamos el certificado
~~~
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd-selfsigned.key -out /etc/ssl/certs/vsftpd-selfsigned.crt
~~~
Ahora entramos al fichero vsftpd.conf y vamos abajo del todo, donde pone rsa
ponemos el certificado que hemos creado
~~~
rsa_cert_file=/etc/ssl/certs/vsftpd-selfsigned.crt
rsa_private_key=/etc/ssl/private/vsftpd-selfsigned.key
ssl_enable=YES
~~~
Reiniciamos el servidor
~~~
sudo systemctl restart vsftpd.service
~~~
Descargamos el fichero que funciona:
~~~
wget https://raw.githubusercontent.com/escartii/escartii/main/VSFTPD/vsftpd.conf
~~~
Creamos el fichero
~~~
sudo nano /etc/vsftpd.chroot_list
~~~
Copiamos esto dentro del fichero que acabamos de crear:
~~~
root:x:0:0:root:/root:/bin/bash
~~~



