# Generated by Django 4.2.3 on 2023-07-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Описание ягод')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно к заказу')),
            ],
            options={
                'verbose_name': 'Опция ягод',
                'verbose_name_plural': 'Опции ягод',
            },
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Описание украшения')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно к заказу')),
            ],
            options={
                'verbose_name': 'Опция украшения',
                'verbose_name_plural': 'Опции украшения',
            },
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_layers', models.IntegerField(verbose_name='Количество слоев')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно к заказу')),
            ],
            options={
                'verbose_name': 'Опция количества слоев',
                'verbose_name_plural': 'Опции количества слоев',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Описание формы')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно к заказу')),
            ],
            options={
                'verbose_name': 'Опция формы',
                'verbose_name_plural': 'Опции формы',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Описание топпинга')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно к заказу')),
            ],
            options={
                'verbose_name': 'Опция топпинга',
                'verbose_name_plural': 'Опции топпинга',
            },
        ),
    ]