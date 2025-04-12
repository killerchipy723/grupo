window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const seccion = params.get('seccion');
    if (seccion) {
      mostrarSeccion(seccion);
    }

    
  });