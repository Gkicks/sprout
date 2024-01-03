# Generated by Django 4.2.8 on 2024-01-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_ingregdients_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(choices=[(0, 'Breakfast'), (1, 'Starter'), (2, 'Main'), (3, 'Snack'), (4, 'Side'), (5, 'Dessert'), (6, 'Drink')], default=2),
        ),
    ]
