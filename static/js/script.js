// universal
const url = window.location.href;

// index.html page
const heroSection = document.getElementById('hero-section');
const page = document.getElementsByClassName('page-of-text');

// create_recipe.html page
const formTitle = document.getElementById("form-title");
const formSubmit = document.getElementById("form-submit-button");

// star ratings
const rating = document.getElementById('average-rating');
const stars = document.getElementsByClassName('star');
const starOne = document.getElementById('star-one');
const starTwo = document.getElementById('star-two');
const starThree = document.getElementById('star-three');
const starFour = document.getElementById('star-four');
const starFive = document.getElementById('star-five');

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
const confirmDeleteBtns = document.getElementById("confirm-delete-btns");


// forms
const commentFormWrapper = document.getElementById("div_id_body");
const ratingFormWrapper = document.getElementById("div_id_rating");


// index.html page

// Adds eventlistener to check if the page has 'Page 1' on it when loaded
// If page is page 1 displays the hero image
if(heroSection) {
    window.addEventListener('load', function () {
    if (page[0].textContent.includes('Page 1')) {
        heroSection.classList.remove('hidden');
        }
    });
}


// create_recipe page

// checks the url to see if a user is creating or editing a comment
// changes the title and submit button depending on what they are trying to do
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


// recipe detail page

// adds eventlistener to get the rating of a recipe
// displays stars showing this rating
if(rating) {
    document.addEventListener('DOMContentLoaded', function () {
        let averageRating = rating.innerText;
        if (averageRating == 1) {
            for (let star of stars) {
                star.classList.add('fa-regular', 'fa-star'); 
            }
            starOne.className = 'star fa-solid fa-star';
        }
        else if (averageRating == 1.5) {
            for (let star of stars) {
                star.classList.add('fa-regular', 'fa-star'); 
            }
            starOne.className = 'star fa-solid fa-star';
            starTwo.className = ' star fa-solid fa-star-half-stroke';
        }
        else if (averageRating == 2) {
            for (let star of stars) {
                star.classList.add('fa-regular', 'fa-star');
            }
            starOne.className = 'star fa-solid fa-star';
            starTwo.className = 'star fa-solid fa-star';
        }
        else if (averageRating == 2.5) {
            for (let star of stars) {
                star.classList.add('fa-regular', 'fa-star'); 
            }
            starOne.className = 'star fa-solid fa-star';
            starTwo.className = 'star fa-solid fa-star';
            starThree.className = 'star fa-solid fa-star-half-stroke';
        }
        else if (averageRating == 3) {
            for (let star of stars) {
                star.classList.add('fa-solid', 'fa-star'); 
            }
            starFour.className = 'start fa-regular fa-star';
            starFive.className = 'start fa-regular fa-star';
        }
        else if (averageRating == 3.5) {
            for (let star of stars) {
                star.classList.add('fa-solid', 'fa-star'); 
            }
            starFour.className = 'star fa-solid fa-star-half-stroke';
            starFive.className = 'start fa-regular fa-star';
        }
        else if (averageRating == 4) {
            for (let star of stars) {
                star.classList.add('fa-solid', 'fa-star'); 
            }
            starFive.className = 'start fa-regular fa-star';
        }
        else if (averageRating == 4.5) {
            for (let star of stars) {
                star.classList.add('fa', 'fa-star'); 
            }
            starFive.className = 'star fa-solid fa-star-half-stroke';
        }
        else if (averageRating == 5) {
            for (let star of stars) {
                star.classList.add('fa-solid', 'fa-star'); 
            }
        }
    });
}

// edit comment

// add eventlistener to each edit button
// gets the id of the comment that button relates to
// puts the current comment into the comment-form text input area
// changes the wording in the submit button to 'update'
// adds action="edit_comment/comment_id" to the comment-form
// scrolls back to the comment-form so it is there for the user to update
for (let button of editButtons) {
    button.addEventListener('click', function() {
        let commentId = this.getAttribute("data-comment-id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentBody.value = commentContent;
        commentBody.style.border = "2px solid var(--dark-green)";
        commentBody.style.height = "6rem";
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
        commentHeader.scrollIntoView({behaviour: 'smooth'});
    }
        );}

// adds eventlisteners to the cancel-delete button
// hides the delete modal when this is pressed
if(deleteModal) {
    cancelDelete.addEventListener("click", function() {
        deleteModal.style.display = "None";
    });
}

// delete comment
// add eventlistener to each delete button
// gets the id of the comment that button relates to
// adds action="delete_comment/comment_id" to the confirm-delete-buttons form
// displays the delete modal
for(let button of deleteButtons) {
    button.addEventListener("click", function() {
        let commentId = this.getAttribute("data-comment-id");
        confirmDeleteBtns.setAttribute("action", `delete_comment/${commentId}`);
        deleteModal.style.display = "block";
    });
}

// adds eventlisteners to the confirm-delete button
// hides the delete modal when this is pressed
if (confirmDelete) {
    confirmDelete.addEventListener("click", function() {
        deleteModal.style.display = "None";
    });
}

// to add a label to the comment form and give it a class of sr-only
if(commentFormWrapper) {
    document.addEventListener("DOMContentLoaded", function() {
        let commentLabel = document.createElement('label');
        commentFormWrapper.insertBefore(commentLabel, commentFormWrapper.firstChild);
        commentLabel.htmlFor = ('id_body');
        commentLabel.classList.add('sr-only');
        commentLabel.innerText = 'Comment';
    });
}

// to add a label to the comment form and give it a class of sr-only
if(ratingFormWrapper) {
    document.addEventListener("DOMContentLoaded", function() {
        let ratingLabel = document.createElement('label');
        ratingFormWrapper.insertBefore(ratingLabel, ratingFormWrapper.firstChild);
        ratingLabel.htmlFor = ('id_rating');
        ratingLabel.classList.add('sr-only');
        ratingLabel.innerText = 'Rating';
    });
}