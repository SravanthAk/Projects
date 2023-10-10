// JavaScript for responsive menu
document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const menuList = document.querySelector('.menu-list');

    menuToggle.addEventListener('click', function () {
        menuList.classList.toggle('active');
    });
});

// JavaScript for contact form validation
document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contact-form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageInput = document.getElementById('message');

    contactForm.addEventListener('submit', function (e) {
        let valid = true;

        if (!nameInput.value.trim()) {
            valid = false;
            alert('Please enter your name.');
        }

        if (!emailInput.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
            valid = false;
            alert('Please enter a valid email address.');
        }

        if (!messageInput.value.trim()) {
            valid = false;
            alert('Please enter a message.');
        }

        if (!valid) {
            e.preventDefault();
        }
    });
});
