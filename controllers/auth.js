const formulario = document.querySelector('form');
const emailInput = document.querySelector('input[name="username"]'); // O "email", según tu HTML
const pass1 = document.querySelector('input[name="password"]');
const pass2 = document.querySelector('input[name="confirm_password"]');

formulario.addEventListener('submit', (evento) => {
    // 1. Expresión Regular para el email (el equivalente a regex_email en Python)
    const regexEmail = /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$/;

    // 2. Validación de formato de Email
    if (!regexEmail.test(emailInput.value)) {
        evento.preventDefault();
        alert("El formato del email no es válido.");
        return; // Salimos de la función para no seguir evaluando
    }

    // 3. Validación de longitud de contraseña (len(password) < 6)
    if (pass1.value.length < 6) {
        evento.preventDefault();
        alert("La contraseña debe tener al menos 6 caracteres.");
        return;
    }

    // 4. Validación de coincidencia (la que ya tenías)
    if (pass1.value !== pass2.value) {
        evento.preventDefault();
        alert("¡Cuidado! Las contraseñas no coinciden.");
        return;
    }
    });