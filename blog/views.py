from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 4


def recipe_detail(request, slug):
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe},
    )
