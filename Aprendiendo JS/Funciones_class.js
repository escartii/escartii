funcionesjs.js
hola

// Funciones JS
// Alvaro Escartí :))
//Forma nueva de hacerlo 

class Inventario {
    constructor(nombre) {
      this.nombre = nombre
      this.articulos = [];
      
    }
    getNombre () {
      return this.nombre
    }
    add(articulo, cantidad) {
      this.articulos[articulo] = cantidad;
    }
    cantidad(articulo) {
      return this.articulos[articulo]
    }
  }
  
  let libros = new Inventario("libros");
  libros.getNombre()
  libros.add("Aprendiendo JavaScript", 5);
  libros.cantidad('Aprendiendo JavaScript')

  //Respuesta 'libros'
  //Respuesta 5
