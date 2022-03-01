"""library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
# from book import views
from book.views import homepage ,edit_data,delete_data
from book.views import show_all_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage ,name = "homepage"),
    path('show-all-books/',show_all_books, name ="show_all_books" ),
    path('edit/<int:id>/', edit_data, name = "edit"),
    path('delete/<int:id>/', delete_data, name = "delete"),

]
