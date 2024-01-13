const formTitle = document.getElementById("form-title");
const formSubmit = document.getElementById("form-submit-button");
const url = window.location.href;

console.log('working');

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