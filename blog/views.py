from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Comment, Rating
from .forms import RecipeForm, CommentForm, RatingForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Avg


class RecipeList(generic.ListView):
    """
    to display a list of all receipes
    """
    template_name = "blog/index.html"
    paginate_by = 8

    def get_queryset(self):
        return Recipe.objects.filter(approved=True)


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
        # ratings = Rating.objects.all()

        return render(
            request,
            "blog/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
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
        elif request.method == 'POST' and 'rating-submit' in request.POST:
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.recipe = recipe
                rating.save()
                messages.success(
                    self.request,
                    'Thank you for rating this recipe')
                comment_form = CommentForm()
                rating_form = RatingForm()
        else:
            comment_form = CommentForm()
            rating_form = RatingForm()
            print('Rating Not Saved')

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

    # def rating_average(request):
    #     queryset = Recipe.objects.all()
    #     recipe = get_object_or_404(queryset, slug=slug)
    #     ratings = recipe.ratings.all()
    #     average = Recipe.objects.aggregate(Avg('rating'))
    #     print('average')

    #     return render(
    #         request,
    #         "blog/recipe_detail.html",
    #         {
    #             "recipe": recipe,
    #             "average": average['avg_integer_field']
    #         }
    #     )

    # def post_rating(self, request, slug, *args, **kwargs):
    #     queryset = Recipe.objects.filter(approved=True)
    #     recipe = get_object_or_404(queryset, slug=slug)
    #     # comments = recipe.comments.all().order_by("created_on")
    #     rating_form = RatingForm(data=request.POST)
    #     if rating_form.is_valid():
    #         rating = rating_form.save(commit=False)
    #         rating.recipe = recipe
    #         # comment.author = self.request.user
    #         rating.save()
    #         messages.success(
    #             self.request,
    #             'Thank you for rating this recipe')
    #         rating_form = RatingForm()
    #     else:
    #         rating_form = RatingForm()

    #     return render(
    #         request,
    #         "blog/recipe_detail.html",
    #         {
    #             "recipe": recipe,
    #             "rating": rating,
    #             "rating_form": rating_form,
    #         },
    #     )

# def comment_form(request):
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.recipe = recipe
#             author = self.request.user
#             comment.save()
#             messages.success(
#                 self.request,
#                 'Comment submitted and awaiting approval')
#         else:
#             comment_form = CommentForm()

#     return render(
#         request,
#         'recipe_detail.html',
#         {
#             'recipe': recipe,
#             'comment': comment,
#             'comment_form': comment_form
#             # 'author': author,
#         }
#     )


class CreateRecipe(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'blog/create_recipe.html'
    success_url = reverse_lazy('home')

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
