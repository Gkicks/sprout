from .models import Recipe, Comment, Rating
from django import forms


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add one ingredient per line',
        'class': 'form-control'
        }))    
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'featured_image', 'category',
                  'ingredients', 'method', 'servings')


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Leave a comment'
    }))
    class Meta:
        model = Comment
        fields = ('body',)


class RatingForm(forms.ModelForm):
    rating = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter a number between 1 and 5',
        'class': 'form-control'
        }))
    class Meta:
        model = Rating
        fields = ('rating',)
