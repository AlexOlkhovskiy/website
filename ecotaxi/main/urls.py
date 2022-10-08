from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.main, name = 'main'),
    path('about', views.about, name = 'about'),
    path('kabinet', views.kabinet, name = 'kabinet'),
    path('rules', views.rules, name = 'rules'),
    path('uslugi', views.uslugi, name = 'uslugi'),
    path('contacts', views.contacts, name = 'contacts'),
    path('dostavka', views.dostavka, name = 'dostavka'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', logout_user, name = 'logout'),
]
