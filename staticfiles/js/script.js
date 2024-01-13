const editButtons = document.getElementsByClassName("edit-btn");
const recipeForm = document.getElementById("recipeForm");


for (let button of editButtons)
    button.addEventListener("click", (e) => {
        const recipeId = e.target.getAttribute("recipe_id");
        recipeForm.setAttribute("action", `edit_recipe / ${recipeId}`);
    });