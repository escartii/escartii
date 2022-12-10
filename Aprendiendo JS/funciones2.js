funciones2.js

// Funciones JS
// Alvaro Escartí :))

function saludar(nombre) {
  return `Hola ${nombre}!`
  //Es lo mismo la forma de arriba que la de abajo 
  return "Hola " + nombre + "!"
  
}

saludar("Javi")
saludar("Alvaro")

//Fuciones de objetos 
function Inventario(nombre) {
  this.nombre = nombre;
  this.articulos = [];
  //es como un array, dentro de los [] se añaden variables
}
Inventario.prototype.getNombre = function() {
  return this.nombre;
}
Inventario.prototype.add = function(articulo, cantidad) {
  this.articulos[articulo] = cantidad;
}
Inventario.prototype.cantidad = function(articulo){
  return this.articulos[articulo]
}

let libros = new Inventario('libros');
libros.getnombre()
libros.add("Aprendiendo JavaScript", 5);
libros.cantidad('Aprendiendo JavaScript');

