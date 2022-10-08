# Generated by Django 3.1.7 on 2021-05-18 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ShopProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='Фото')),
                ('description_small', models.CharField(max_length=250, verbose_name='Краткое описание')),
                ('description_big', models.TextField(verbose_name='Подробное описание')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('code', models.CharField(max_length=20, verbose_name='Артикул')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('manufacturer', models.CharField(max_length=200, verbose_name='Производитель')),
                ('material', models.CharField(max_length=200, verbose_name='Материал')),
                ('size', models.CharField(max_length=200, verbose_name='Размер')),
                ('color', models.CharField(max_length=200, verbose_name='Цвет')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id', 'title', 'code', 'color'],
            },
        ),
    ]