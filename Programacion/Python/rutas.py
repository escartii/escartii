import os

# La ruta del directorio que quieres comprobar
directory = "/home/escartii"

# Comprobación de si el directorio existe
if os.path.exists(directory):
    print("El directorio " + directory +  "existe")
else:
    print("El directorio " + directory + " no existe")
