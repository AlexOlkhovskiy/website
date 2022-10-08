from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# функция для работы с категориями продуктов и продуктами
def show_category(request, cat_slug):
    # присваиваем переменной весь список категорий
    cats = Category.objects.all()
    # присваиваем переменной весь список подкатегорий
    subcats = Subcategory.objects.all()
    # присваиваем переменной ту категорию, слаг которой совпадает со слагом в url-адресе
    catss = Category.objects.get(slug = cat_slug)
    # присваиваем переменной все продукты выбранной категории
    products = ShopProducts.objects.filter(cat_id = catss.pk)

    items_on_page = 4
    paginator = Paginator(products, items_on_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    first_five_pages = list()
    if paginator.num_pages >= 5:
        for x in range(1, 6):
            first_five_pages.append(x)
    else:
        for x in range(1, paginator.num_pages + 1):
            first_five_pages.append(x)
    last_five_pages = list()
    for x in range(paginator.num_pages - 4, paginator.num_pages + 1):
        last_five_pages.append(x)
    if paginator.num_pages == 4:
        last_five_pages.pop(0)
    last_page_2 = paginator.num_pages - 2
    last_page = last_page_2 + 2

    context = {
        'products': products,
        'cats': cats,
        'subcats': subcats,
        'cat_slug': cat_slug,
        'page_obj': page_obj,
        'first_five_pages': first_five_pages,
        'last_five_pages': last_five_pages,
        'last_page_2': last_page_2,
        'last_page': last_page,
        'num_pages': num_pages,
    }
    return render(request, 'shop/category.html', context = context)


def shop(request):
    return render(request, 'shop/shop.html')


def shop_category(request):
    return render(request, 'shop/category.html')


# функция для добавления нового продукта в БД
def shop_add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddProductForm()
    return render(request, 'shop/add_product.html', {'form': form})
