"""
URL configuration for mindful project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home, name="home"),
    path('add/',add, name="add"),
    path('chat/',chat, name="chat"),
    path('delete_entry/<int:entry_id>/', delete_entry, name='delete_entry'),
    path('send_message/', send_message, name='send_message'),

    path('register/',register, name="register"),
    path('login/',login_page, name="login_page"),
    path('logout/',logout_page, name="logout_page"),
]
