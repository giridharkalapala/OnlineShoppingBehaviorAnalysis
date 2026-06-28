// Login Form Validation

document.addEventListener("DOMContentLoaded", function () {

    const loginForm = document.getElementById("loginForm");

    if (loginForm) {

        loginForm.addEventListener("submit", function (e) {

            const email = document.querySelector('input[name="email"]').value.trim();
            const password = document.querySelector('input[name="password"]').value.trim();

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

            if (password === "") {
                alert("Please enter your password.");
                e.preventDefault();
                return;
            }

        });

    }

});