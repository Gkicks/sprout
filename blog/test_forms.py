from django.test import TestCase
from .forms import RecipeForm, CommentForm, RatingForm
from .models import Recipe


class TestRecipeForm(TestCase):
    """
    test to check if the recipe form is valid
    """
    def test_form_is_valid(self):
        """
        correct details entered
        """
        recipe_form = RecipeForm({
            'recipe_name': 'cherry Pie',
            'category': '2',
            'ingredients': '1 spoonful of sugar',
            'method': 'bake in a pie',
            'servings': '4'
        })
        self.assertTrue(
            recipe_form.is_valid(), msg="recipe form is not valid")

    # recipe_name field
    def test_recipe_name_empty(self):
        """
        empty recipe_name
        """
        recipe_form = RecipeForm({'recipe_name': ''})
        self.assertFalse(
            recipe_form.is_valid(), msg="form valid with empty recipe_name")

    def test_recipe_name_too_long(self):
        """
        recipe_name more than 255 characters
        """
        recipe_form = RecipeForm(
            {'recipe_name': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw'
                'xyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef'
                'ghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno'
                'pqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx'
                'yzabcdefghijklmnopqrstuvwxyz'}
                            )
        self.assertFalse(
            recipe_form.is_valid(), msg="form valid with 260 characters")

    
class TestCommentForm(TestCase):
    """
    test to check if the comment form is valid
    """
    def test_form_is_valid(self):
        """
        string entered
        """
        comment_form = CommentForm({'body': 'I love this recipe'})
        self.assertTrue(
            comment_form.is_valid(), msg="comment form is not valid")

    def test_form_is_not_valid(self):
        """
        empty string entered
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(
            comment_form.is_valid(), msg="form is valid with empty string")


class TestRatingForm(TestCase):
    """
    test to check if the rating form is valid
    """
    def test_form_is_valid(self):
        """
        valid number entered
        """
        rating_form = RatingForm({'rating': '1'})
        self.assertTrue(rating_form.is_valid(), msg="rating form is not valid")

    def test_form_is_not_valid_empty(self):
        """
        empty string entered
        """
        rating_form = RatingForm({'rating': ''})
        self.assertFalse(
            rating_form.is_valid(), msg="form is valid with empty string")

    def test_form_is_not_valid_other_int(self):
        """
        integer outside range 1-5 entered
        """
        rating_form = RatingForm({'rating': '6'})
        self.assertFalse(
            rating_form.is_valid(),
            msg="form is valid with int not in range 1-5")

    def test_form_is_not_valid_negative(self):
        """
        negative number entered
        """
        rating_form = RatingForm({'rating': '-5'})
        self.assertFalse(
            rating_form.is_valid(), msg="form is valid with negative number")

    def test_form_is_not_valid_letter(self):
        """
        letter entered
        """
        rating_form = RatingForm({'rating': 'j'})
        self.assertFalse(
            rating_form.is_valid(), msg="rating form is valid with letter")

    def test_form_is_not_valid_special(self):
        """
        special character entered
        """
        rating_form = RatingForm({'rating': '%'})
        self.assertFalse(
            rating_form.is_valid(), msg="form is valid with special character")
