from .models import Recipe, Comment, Rating
from django import forms


class RecipeForm(forms.ModelForm):
    """
    A form for the user to add a recipe
    Placeholder to instruct the user to add each ingredient 
        and method on a new line
    Class to decrease the size of the placeholder on screens less than 435px
    """
    ingredients = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Add one ingredient per line',
        }))
    method = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Add a blank line between each method',
        }))   
    # featured_image = forms.CharField(widget=forms.Image(attrs={
    #     'class': 'form-image',
    #     }))  
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'featured_image', 'category',
                  'ingredients', 'method', 'servings')


class CommentForm(forms.ModelForm):
    """
    Form for the user to leave a comment
    Removes the label from the form
    Placeholder to inform the user what the form is for
    """
    body = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Leave a comment',
    }))
    class Meta:
        model = Comment
        fields = ('body',)


class RatingForm(forms.ModelForm):
    """
    Form to allow the user to leave a rating for the recipe
    Placeholder to say it needs to be a number between 1 and 5
    Class to decrease the size of the placeholder on screens less than 435px
    """
    rating = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter a number between 1 and 5',
        'class': 'form-control'
        }))
    class Meta:
        model = Rating
        fields = ('rating',)