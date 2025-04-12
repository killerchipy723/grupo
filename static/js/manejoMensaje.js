
  window.addEventListener('load', () => {
    const flashes = document.querySelectorAll('.flash-message');
    if (flashes.length > 0) {
      setTimeout(() => {
        flashes.forEach(flash => {
          flash.classList.add('fade-out');
          setTimeout(() => {
            flash.remove(); // o flash.style.display = "none";
          }, 1000); // tiempo para que se complete la transición
        });
      }, 4000); // Espera 4 segundos antes de comenzar la transición
    }
  });

