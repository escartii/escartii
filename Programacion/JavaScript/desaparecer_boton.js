//Alvaro Escarti :))

// Creamos el boton

<button id="Boton">Haz clic aquí</button>

  // Obtener el elemento del botón
  var boton = document.getElementById('Boton');

  // Añadir un click al botón
  boton.addEventListener('click', function() {
    // Hacer desaparecer el botón
    boton.style.display = 'none';
  });

// Para añadirlo al html debemos meterlo dentro de la etiqueta
// <script> </script>

