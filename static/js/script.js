const formTitle = document.getElementById("form-title");
const formSubmit = document.getElementById("form-submit-button");
const url = window.location.href;
const heroSection = document.getElementById('hero-section');
const page = document.getElementsByClassName('page-of-text');

window.addEventListener('load', function () {
    if (url.includes('edit_recipe')) {
        formTitle.innerHTML = 'Edit Recipe';
        formSubmit.innerHTML = 'Update Recipe';
    }
    else {
        formTitle.innerHTML = 'Add Recipe';
        formSubmit.innerHTML = 'Submit Recipe';
    }
});

window.addEventListener('load', function () {
    if (page[0].textContent.includes('Page 1')) {
        heroSection.classList.remove('hidden');
    }
});