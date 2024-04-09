# Generated by Django 3.2.16 on 2024-04-09 12:44

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'default_related_name': 'favorites', 'verbose_name': 'Избранное', 'verbose_name_plural': 'избранные'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Рецепт', 'verbose_name_plural': 'рецепты'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'default_related_name': 'shopping_cart', 'verbose_name': 'Корзина покупок', 'verbose_name_plural': 'корзина покупок'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное время приготовления -\n                 1 минута!'), django.core.validators.MaxValueValidator(1440, message='Максимальное значение должно быть не более 1440 минут')], verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Должен быть минимум\n                        1 ингредиент'), django.core.validators.MaxValueValidator(10000, message='Максимальное значение должно быть не более\n                        10000!')], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=7, samples=None, unique=True, verbose_name='Цвет'),
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name', 'measurement_unit'), name='unique_name_ingredient_measurement_unit'),
        ),
    ]
