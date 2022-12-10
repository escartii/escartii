#Alvaro Escarti :))

# Libraries absolute needed
import os.path

# Variables
path="/client"

if os.path.ismount(path):
    print("La ruta: " + path + ", esta montada")
else:
    print("La ruta no esta montada")

