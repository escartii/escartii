#Alvaro Escarti :))

#Saber todas las cosas que podemos hacer con un string, operar, cortar, buscar, etc...
myString="hola mundo"
print("la variable es: " + myString) 
print(f"la variable es: {myString}") #La f es para decirle que estamos definiendo en la llave una variable que está arriba

#print(dir(myString)) #Muestra todas las opciones con un string
#ejemplo
print(myString.upper())# Mostrar la variable en mayusculas
print(myString.capitalize()) #La primera letra en mayuscula
print(myString.replace('hello', 'alvaro')) #Sustituir la primera palabra por otra
print(myString.count("a")) #Contar cuantas veces aparece el caracter 'a' || el caracter vacio siempre será 1
print(myString.startswith("hola")) #Comprobar si la variable empieza por "hola"
print(myString.endswith("Mundo")) #Comprobar si la variable termina por "mundo"
print(myString.split()) # Separar una variable 
print(myString.find(" ")) #Nos muestra la posicion en la que se encuentra el caracter || el primero siempre será 0
print(len(myString)) #Nos muestra la longitud de la variable
print(myString.isnumeric()) #Nos muestra si la variable es numerico
print(myString.isalpha()) #Nos muestra si la variable es alfanumerica
print(myString[4])
