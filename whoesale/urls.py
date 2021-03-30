"""whoesale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from user import views as user_view
from blog import views as blog_view
from product import views as product_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view.aboutPage, name='user-about'),
    path('register/', user_view.signup, name = 'register'),
    path('base/', user_view.basePage),
    path('product/', product_view.product),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='user/logout.html'),name='logout'),
    path('home/', blog_view.homepage, name = 'homepage')
]
# path('login/', user_view.login),