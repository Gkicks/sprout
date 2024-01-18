from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

CATEGORY = ((0, 'Breakfast'), (1, 'Starter'), (2, 'Main'),
            (3, 'Snack'), (4, 'Side'), (5, 'Dessert'), (6, 'Drink'))


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(
        max_length=255, populate_from='recipe_name', editable=True,
        always_update=True,)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_author')
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.IntegerField(choices=CATEGORY, default=2)
    ingredients = models.TextField(blank=False)
    method = models.TextField(blank=False)
    servings = models.IntegerField(validators=[
        MinValueValidator(1)], blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.recipe_name


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commentor')
    body = models.TextField(validators=[MinLengthValidator(3)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.body


class Rating(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField(blank=True, default=0, validators=[
        MinValueValidator(1), MaxValueValidator(5)],)

    def __str__(self):
        return str(self.rating)

    # @property
    # def average_rating(self):
    #     return self.rating.all().aggregate(Avg('rating')).get('rating__avg', 0.00)