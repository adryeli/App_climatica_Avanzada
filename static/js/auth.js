document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registroForm");
  if (!form) return;

  const email = document.getElementById("email");
  const password = document.getElementById("password");
  const emailError = document.getElementById("emailError");
  const passwordError = document.getElementById("passwordError");

  form.addEventListener("submit", (e) => {
    let valid = true;

    emailError.textContent = "";
    passwordError.textContent = "";

    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailRegex.test(emailValue)) {
      emailError.textContent = "Introduce un correo electrónico válido.";
      valid = false;
    }

    if (passwordValue.length < 6) {
      passwordError.textContent = "La contraseña debe tener al menos 6 caracteres.";
      valid = false;
    }

    if (!valid) {
      e.preventDefault();
    }
  });
});

const loginForm = document.getElementById("loginForm");

if (loginForm) {
  loginForm.addEventListener("submit", (e) => {
    let valid = true;

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");

    emailError.textContent = "";
    passwordError.textContent = "";

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailRegex.test(email)) {
      emailError.textContent = "Email no válido";
      valid = false;
    }

    if (password.length === 0) {
      passwordError.textContent = "Introduce la contraseña";
      valid = false;
    }

    if (!valid) e.preventDefault();
  });
}