from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm

# Create your views here.


class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 4


def recipe_detail(request, slug):
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
    recipe_form = RecipeForm
    if request.method == 'POST':
        context = {
            'recipe_form': recipe_form,
        }
    return render(
        request,
        'blog/add_recipe.html',
        {
            "recipe_form": recipe_form,
        })
