"""exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin

from django.urls import path, include

from mainpage.views import main_page, hello_world, hello_personalized
from maths.views import math_operations,math_list,math_details
#zjazd_5.Django_examples.exercises.
from products.views import fake_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('hello', hello_world),
    path('hello/<name>/<lastname>', hello_personalized), #ostre nawiasy mówią o tym, że jest to zmeienna
    path('maths', math_list),
    path('maths/<int:id>', math_details),
    path('maths/<operations>/<int:a>/<int:b>', math_operations),
    path('products', fake_view),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]