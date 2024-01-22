from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Comment, Rating
from .forms import RecipeForm, CommentForm, RatingForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Avg
from django.contrib.auth.decorators import login_required


class RecipeList(generic.ListView):
    """
    to display a list of all receipes
    """
    Model = Recipe
    template_name = "blog/index.html"
    paginate_by = 8
    queryset = Recipe.objects.filter(approved=True)
    for recipe in queryset:
        average_rating = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']
        recipe.average_rating = round(average_rating*2)/2 if average_rating else None
        recipe.save()
        print(recipe)
        print(recipe.average_rating)


class RecipeDetailView(generic.DetailView):
    """
    returns a view of the full recipe
    displays comments under the recipe
    shows a form for the user to leave a new comment
    """
    model = Recipe

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.all().order_by("created_on")
        average_rating = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']
        average_number = round(average_rating*2)/2 if average_rating else None

        return render(
            request,
            "blog/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "average_number": average_number,
                "comment_form": CommentForm(),
                "rating_form": RatingForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.all().order_by("created_on")
        comment_form = CommentForm(data=request.POST)
        rating_form = RatingForm(data=request.POST)
        comment = None
        rating = None
        if request.method == 'POST' and 'comment-submit' in request.POST:
            rating = None
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.author = self.request.user
                comment.save()
                messages.success(
                    self.request,
                    'Comment submitted and awaiting approval')
                rating_form = RatingForm()
                comment_form = CommentForm()
                return HttpResponseRedirect(request.path_info)
        elif request.method == 'POST' and 'rating-submit' in request.POST:
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.recipe = recipe
                rating.save()
                messages.success(
                    self.request,
                    'Thank you. Your rating has been submitted')
                comment_form = CommentForm()
                rating_form = RatingForm()
                return HttpResponseRedirect(request.path_info)
        else:
            comment_form = CommentForm()
            rating_form = RatingForm()

        return render(
            request,
            "blog/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "comment_form": comment_form,
                "rating": rating,
                "rating_form": rating_form,
            },
        )


@login_required 
def edit_comment(request, slug, comment_id):
    instance = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=instance)
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.edited = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR,
                                'Error updating comment')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def delete_comment(request, slug, comment_id):
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class CreateRecipe(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'blog/create_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        # ingredients = ingredients.split
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

    for recipe in user_recipes:
        average_rating = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']
        recipe.average_rating = round(average_rating*2)/2 if average_rating else None
    
    return render(
        request,
        'blog/my_recipes.html',
        {
            "user_recipes": user_recipes,
        })


class EditRecipe(UserPassesTestMixin, UpdateView):
    queryset = Recipe.objects.all()
    form_class = RecipeForm
    template_name = 'blog/create_recipe.html'
    success_url = reverse_lazy('user_recipes')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.approved = False
        messages.success(
            self.request,
            'Recipe updated and awaiting approval')

        return super().form_valid(form)


class DeleteRecipe(UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'blog/confirm-delete.html'
    contect_object_name = 'recipe'
    success_url = reverse_lazy('user_recipes')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your recipe has been deleted')

        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        return HttpResponseRedirect(success_url)
