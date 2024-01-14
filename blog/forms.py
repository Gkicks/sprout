from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'featured_image', 'category',
                     'ingredients', 'method', 'servings')
        # exclude = ('author',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
