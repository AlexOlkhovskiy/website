from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import RegisterUserForm


def main(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def kabinet(request):
    return render(request, 'main/kabinet.html')


def rules(request):
    return render(request, 'main/rules.html')


def uslugi(request):
    return render(request, 'main/uslugi.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def dostavka(request):
    return render(request, 'main/dostavka.html')


def register_user1(request):
    return render(request, 'main/rules.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('register')

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('about')
# функция для добавления нового продукта в БД
# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('about')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'main/register.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('about')


def logout_user(request):
    logout(request)
    return redirect('login')
