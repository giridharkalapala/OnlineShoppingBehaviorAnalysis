// ===============================
// NAVBAR BACKGROUND
// ===============================

window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 80) {

        navbar.style.background = "#0f172a";

        navbar.style.padding = "12px 0";

        navbar.style.transition = ".3s";

    }

    else {

        navbar.style.background = "";

        navbar.style.padding = "18px 0";

    }

});


// ===============================
// SMOOTH SCROLL
// ===============================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});


// ===============================
// COUNTER ANIMATION
// ===============================

function animateCounter(id, target, duration = 2000) {

    const element = document.getElementById(id);

    if (!element) return;

    let start = 0;

    const increment = target / (duration / 20);

    const timer = setInterval(() => {

        start += increment;

        if (start >= target) {

            start = target;

            clearInterval(timer);

        }

        element.innerHTML = Math.floor(start) + "+";

    }, 20);

}


window.onload = function () {

    animateCounter("customers", 5000);

};


// ===============================
// FADE-IN ANIMATION
// ===============================

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.style.opacity = "1";

            entry.target.style.transform = "translateY(0px)";

        }

    });

});

document.querySelectorAll("section").forEach(section => {

    section.style.opacity = "0";

    section.style.transform = "translateY(40px)";

    section.style.transition = "all 1s";

    observer.observe(section);

});


// ===============================
// CONTACT FORM
// ===============================

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function (e) {

        e.preventDefault();

        alert("Thank you! Your message has been received.");

        form.reset();

    });

}