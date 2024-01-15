from .models import Recipe, Comment, Rating
from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, submit
# from crispy_forms.bootstrap import FormActions


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'featured_image', 'category',
                  'ingredients', 'method', 'servings')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)
