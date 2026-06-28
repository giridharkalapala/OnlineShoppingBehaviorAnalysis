// Register Form Validation

document.addEventListener("DOMContentLoaded", function () {

    const registerForm = document.getElementById("registerForm");

    if (registerForm) {

        registerForm.addEventListener("submit", function (e) {

            const name = document.querySelector('input[name="name"]').value.trim();
            const email = document.querySelector('input[name="email"]').value.trim();
            const password = document.querySelector('input[name="password"]').value.trim();

            if (name === "") {
                alert("Please enter your name.");
                e.preventDefault();
                return;
            }

            if (email === "") {
                alert("Please enter your email.");
                e.preventDefault();
                return;
            }

            if (!email.includes("@")) {
                alert("Please enter a valid email.");
                e.preventDefault();
                return;
            }

            if (password.length < 6) {
                alert("Password must be at least 6 characters.");
                e.preventDefault();
                return;
            }

        });

    }

});