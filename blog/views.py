from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class RecipeList(generic.ListView):
    """
    to display a list of all receipes
    """
    template_name = "blog/index.html"
    paginate_by = 8

    def get_queryset(self):
        return Recipe.objects.filter(approved=True)


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


class CreateRecipe(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'blog/create_recipe.html'
    success_url = reverse_lazy('home')
    # success_message = 'Recipe submitted and awaiting approval'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request,
            'Recipe submitted and awaiting approval')

        return super().form_valid(form)


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


# class EditRecipe(UpdateView):
#     form_class = RecipeForm
#     template_name = 'blog/create_recipe.html'
#     success_url = reverse_lazy('home')
    # success_message = 'Recipe submitted and awaiting approval'

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     messages.success(
    #         self.request,
    #         'Recipe submitted and awaiting approval')

    #     return super().form_valid(form)
