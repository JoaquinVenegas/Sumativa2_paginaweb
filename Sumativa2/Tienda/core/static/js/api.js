const url = 'https://api.adviceslip.com/advice';

fetch(url)
  .then(response => {
    // Verifica si la respuesta es exitosa
    if (response.ok) {
      // Devuelve los datos como JSON
      return response.json();
    }
    // Si la respuesta no es exitosa, lanza un error
    throw new Error('No hay respuesta del servidor: ');
  })
  .then(data => {
    // Maneja los datos recibidos
    console.log(data);
    if (data && data.slip && data.slip.advice) {
      var consejo = data.slip.advice;
      // Hacer algo con el consejo, como mostrarlo en la página
      document.getElementById('consejo').textContent = consejo;
    } else {
      console.error("No se pudo obtener el consejo del día: ");
    }
  })
  .catch(error => {
    // Maneja los errores
    console.error('Problema al realizar el fetch: ', error);
  });
