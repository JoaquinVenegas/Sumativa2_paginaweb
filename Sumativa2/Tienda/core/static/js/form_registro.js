$(document).ready(function(){
    
        function validateForm() {
        var nombre_usuario = $("#in_usuario").val();
        var email = $("#in_correo").val();
        var password = $("#in_password").val();
        var pasword2 = $("#in_password2").val();
        var fecha_nac = $("#in_fecha").val();
    
        // Validación campos vacíos
        if (nombre_usuario == "" || email == "" ||
            password == "" || pasword2 == "" || fecha_nac == "" )
        {
            alert("Debe ingresar campos obligatorios");
            return false;
        }

         // Validar el formato del correo electrónico
        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        if (!emailPattern.test(email)) {
            alert("El correo electrónico no tiene un formato válido");
            return false;
        }
        
        // Validación de rango de longitud de contraseña entre 6 y 18 caracteres
        var passwordPattern = /^(?=.*\d)(?=.*[A-Z]).{6,12}$/;
        if (!passwordPattern.test(password)) {
            alert("La contraseña debe contener al menos un número y una letra en mayúscula y tener entre 6 y 12 caracteres");
            return false;
        }

        // Validación que las dos contraseñas sean iguales
        if (password != pasword2)
        {
            alert("Contraseñas no coinciden");
            return false;
        }

        //Validacion para ver si tiene 18 años
        var today = new Date();
        var birthDateObj = new Date(fecha_nac);
        var age = today.getFullYear() - birthDateObj.getFullYear();

        // Comprobar si ya ha pasado el cumpleaños de este año
        if (today.getMonth() < birthDateObj.getMonth() || (today.getMonth() === birthDateObj.getMonth() && today.getDate() < birthDateObj.getDate())) {
        age--;
        }

        if (age < 18) {
        alert("Debes tener al menos 18 años para registrarte");
        return false;
        }

    //Si todas las validacion son exitosas, entonces se enviara
    return true;
    }

     // Manejar el evento de envío del formulario
     $("#registroForm").submit(function(event) {
        // Llamar a la función de validación
        if (!validateForm()) {
          event.preventDefault(); // Evitar el envío del formulario si la validación falla
        }
      });
});