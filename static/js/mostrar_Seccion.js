function mostrarSeccion(id) {
    // Oculta todas
    document.querySelectorAll('.seccion').forEach(sec => sec.classList.remove('visible'));
  
    // Muestra solo la que coincide
    const visible = document.getElementById(id);
    if (visible) visible.classList.add('visible');
  }
  
  // ✅ Ejecutar cuando la página carga
  window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const seccion = params.get('seccion');
  
    if (seccion) {
      mostrarSeccion(seccion);
    }
  });
  