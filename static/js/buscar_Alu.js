const input = document.getElementById('buscador');
const lista = document.getElementById('sugerencias');
const inputOcultoIdAlumno = document.getElementById('idalumno'); // input oculto

input.addEventListener('input', () => {
  const query = input.value.trim();
  lista.innerHTML = '';

  if (query === '') {
    lista.style.display = 'none';
    return;
  }

  fetch(`/buscar_alumnos?q=${encodeURIComponent(query)}`)
    .then(res => res.json())
    .then(data => {
      if (data.length === 0) {
        lista.style.display = 'none';
        return;
      }

      data.forEach(alumno => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'list-group-item-action');
        li.textContent = `${alumno.nombre} - ${alumno.dni}`;

        li.onclick = () => {
          input.value = `${alumno.nombre} - ${alumno.dni}`;
          inputOcultoIdAlumno.value = alumno.idalumno; // guardamos el ID
          lista.innerHTML = '';
          lista.style.display = 'none';
        };

        lista.appendChild(li);
      });

      lista.style.display = 'block';
    });
});
