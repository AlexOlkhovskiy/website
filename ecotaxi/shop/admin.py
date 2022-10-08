from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'code', 'date', 'color', 'size')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description_small', 'description_big', 'code')
    list_filter = ('date',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class Subcategory2ndLvlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ShopProducts, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Subcategory2ndLvl, Subcategory2ndLvlAdmin)



