from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class RecipeList(generic.ListView):
    """
    to display a list of all receipes
    """
    template_name = "blog/index.html"
    paginate_by = 8

    def get_queryset(self):
        return Recipe.objects.all()


class RecipeDetailView(generic.DetailView):
    model = Recipe

    def recipe_detail(self, request, slug):
        """
        returns a view of the full recipe
        """
        queryset = Recipe.objects.filter(approved=True)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.all().order_by("created_on")
        comment_count = recipe.comments.filter(approved=True).count()

        return render(
            request,
            "blog/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "comment_count": comment_count,
            },
        )


def add_recipe(request):
    """
    user to complete form to add a recipe and this to save to the database
    redirects back to the home page when valid form is submitted
    sucess message displayed
    """
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Recipe submitted and awaiting approval')
            return HttpResponseRedirect(reverse(''))
    else:
        recipe_form = RecipeForm
    return render(
        request,
        'blog/add_recipe.html',
        {
            "recipe_form": recipe_form,
        })


def user_recipes(request):
    """
    return a list of recipes where the logged in user is the author
    """
    user_recipes = Recipe.objects.filter(
        author=request.user).order_by('-created_on')
    return render(
        request,
        'blog/my_recipes.html',
        {
            "user_recipes": user_recipes,
        })
