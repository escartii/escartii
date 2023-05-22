#Alvaro Escarti :))

def verificar_ip(ip):
    # Verificar que la dirección IP tenga el formato correcto
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or int(parte) < 0 or int(parte) > 255:
            return False
    return True

def convertir_a_binario(ip):
    partes = ip.split('.')
    binario = []
    for parte in partes:
        binario.append(bin(int(parte))[2:].zfill(8))  # Convertir cada parte a binario y completar con ceros a la izquierda
    return '.'.join(binario)

# Pedir al usuario que ingrese una dirección IP
direccion_ip = input("Ingresa una dirección IP: ")

# Verificar y convertir la dirección IP
if verificar_ip(direccion_ip):
    binario = convertir_a_binario(direccion_ip)
    print("Dirección IP en binario:", binario)
else:
    print("La dirección IP ingresada es inválida.")
