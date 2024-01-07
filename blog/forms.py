from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'featured_image', 'category',
                  'content', 'ingredients', 'method', 'servings')
