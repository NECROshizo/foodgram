# Generated by Django 4.2.1 on 2023-05-15 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='favorit_recipes', to=settings.AUTH_USER_MODEL, verbose_name='В избраном'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='food.IngredientsRecipes', to='food.ingredients', verbose_name='Ингредиенты'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='food.tag', verbose_name='Таг'),
        ),
        migrations.AddField(
            model_name='ingredientsrecipes',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_in_recipe', to='food.ingredients', verbose_name='Ингредиент'),
        ),
        migrations.AddField(
            model_name='ingredientsrecipes',
            name='recipes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_in_recipe', to='food.recipes', verbose_name='Рецепт'),
        ),
        migrations.AddConstraint(
            model_name='ingredients',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_ingredient'),
        ),
        migrations.AddConstraint(
            model_name='recipes',
            constraint=models.UniqueConstraint(fields=('author', 'name', 'pub_date'), name='unique_recipes'),
        ),
        migrations.AddConstraint(
            model_name='ingredientsrecipes',
            constraint=models.UniqueConstraint(fields=('ingredient', 'recipes'), name='unique_ingredient_to_recipes'),
        ),
    ]
