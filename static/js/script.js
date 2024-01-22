const url = window.location.href;

// index.html page
const heroSection = document.getElementById('hero-section');
const page = document.getElementsByClassName('page-of-text');

// create_recipe.html page
const formTitle = document.getElementById("form-title");
const formSubmit = document.getElementById("form-submit-button");

// star ratings
const rating = document.getElementById('average-rating')
const stars = document.getElementsByClassName('star')
const starOne = document.getElementById('star-one')
const starTwo = document.getElementById('star-two')
const starThree = document.getElementById('star-three')
const starFour = document.getElementById('star-four')
const starFive = document.getElementById('star-five')


// edit comment
const editButtons = document.getElementsByClassName("edit-btn");
const commentBody = document.getElementById("id_body");
const commentForm = document.getElementById("comment-form");
const submitButton = document.getElementById("form-submit-btn");
const commentHeader = document.getElementById("comment-header");


// delete comment
const deleteModal = document.getElementById("delete-modal");
const deleteButtons = document.getElementsByClassName("delete-btn");
const confirmDelete = document.getElementById("confirm-delete");
const cancelDelete = document.getElementById("cancel-delete");
const confirmDeleteBtns = document.getElementById("confirm-delete-btns")

// create_recipe page
window.addEventListener('load', function () {
    if (url.includes('edit_recipe')) {
        formTitle.innerHTML = 'Edit Recipe';
        formSubmit.innerHTML = 'Update Recipe';
    }
    else if (url.includes('create_recipe')) {
        formTitle.innerHTML = 'Add Recipe';
        formSubmit.innerHTML = 'Submit Recipe';
    }
});

// index.html page
window.addEventListener('load', function () {
    if (page[0].textContent.includes('Page 1')) {
        heroSection.classList.remove('hidden');
    }
});

// all html pages
window.addEventListener('load', function () {
    let averageRating = rating.innerText
    if (averageRating == 1) {
        for (let star of stars) {
            star.classList.add('fa-regular', 'fa-star') 
        }
        starOne.classList = 'star fa-solid fa-star'
    }
    else if (averageRating == 1.5) {
        for (let star of stars) {
            star.className = 'fa-regular, fa-star' 
        }
        starOne.className = 'star fa-solid fa-star'
        starTwo.className = ' star fa-solid fa-star-half-stroke'
    }
    else if (averageRating == 2) {
        for (let star of stars) {
            star.classList.add('fa-regular', 'fa-star') 
        }
        starOne.className = 'star fa-solid fa-star'
        starTwo.className = 'star fa-solid fa-star'
    }
    else if (averageRating == 2.5) {
        for (let star of stars) {
            star.classList.add('fa-regular', 'fa-star') 
        }
        starOne.className = 'star fa-solid fa-star'
        starTwo.className = 'star fa-solid fa-star'
        starThree.className = 'star fa-solid fa-star-half-stroke'
    }
    else if (averageRating == 3) {
        for (let star of stars) {
            star.classList.add('fa-solid', 'fa-star') 
        }
        starFour.className = 'start fa-regular fa-star'
        starFive.className = 'start fa-regular fa-star'
    }
    else if (averageRating == 3.5) {
        for (let star of stars) {
            star.classList.add('fa-solid', 'fa-star') 
        }
        starFour.className = 'star fa-solid fa-star-half-stroke'
        starFive.className = 'start fa-regular fa-star'
    }
    else if (averageRating == 4) {
        for (let star of stars) {
            star.classList.add('fa-solid', 'fa-star') 
        }
        starFive.className = 'start fa-regular fa-star'
    }
    else if (averageRating == 4.5) {
        for (let star of stars) {
            star.classList.add('fa', 'fa-star') 
        }
        starFive.className = 'star fa-solid fa-star-half-stroke'
    }
    else if (averageRating == 5) {
        for (let star of stars) {
            star.classList.add('fa-solid', 'fa-star') 
        }
    }
})





for (let button of editButtons) {
    button.addEventListener('click', function() {
        let commentId = this.getAttribute("data-comment-id")
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentBody.value = commentContent
        submitButton.innerText = "Update"
        commentForm.setAttribute("action", `edit_comment/${commentId}`)
        commentHeader.scrollIntoView({behaviour: 'smooth'})
    }
        )}


// delete comment
for(let button of deleteButtons) {
    button.addEventListener("click", function() {
        let commentId = this.getAttribute("data-comment-id")
        confirmDeleteBtns.setAttribute("action", `delete_comment/${commentId}`)
        deleteModal.style.display = "block"
    })
}

cancelDelete.addEventListener("click", function() {
    deleteModal.style.display = "None"
})

confirmDelete.addEventListener("click", function() {
    deleteModal.style.display = "None"
})