from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class ShopProducts(models.Model):
    title = models.CharField('Название', max_length = 50)
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = 'URL')
    photo = models.ImageField(upload_to = "photo/", verbose_name = "Фото")
    description_small = models.CharField('Краткое описание', max_length = 250)
    description_big = models.TextField('Подробное описание')
    date = models.DateTimeField('Дата публикации')
    code = models.CharField('Артикул', max_length = 20)
    price = models.CharField('Цена', max_length = 20)
    manufacturer = models.CharField('Производитель', max_length = 200)
    material = models.CharField('Материал', max_length = 200)
    size = models.CharField('Размер', max_length = 200)
    color = models.CharField('Цвет', max_length = 200)
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now = True, verbose_name = 'Время изменения')
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id', 'title', 'code', 'color']


class Category(models.Model):
    name = models.CharField('Категория', max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = 'URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField('Подкатегория', max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = 'URL')
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Категория', null = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs = {'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Subcategory2ndLvl(models.Model):
    name = models.CharField('Подкатегория 2 уровень', max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = 'URL')
    cat = models.ForeignKey('Subcategory', on_delete = models.PROTECT, verbose_name = 'Категория', null = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs = {'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Подкатегория 2 уровень'
        verbose_name_plural = 'Подкатегории 2 уровень'

