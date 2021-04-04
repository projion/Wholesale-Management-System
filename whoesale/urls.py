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
from django.urls import path, include
from user import views as user_view
from blog import views as blog_view
from product import views as product_view
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view.aboutPage, name='about'),
    path('register/', user_view.signup, name = 'register'),
    path('base/', user_view.basePage, name='base'),
    path('product/', include('product.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='user/logout.html'),name='logout'),
    path('homepage/', blog_view.homepage, name = 'homepage'),
    path('contact/', blog_view.contactPage, name='contact'),
    path('home/', user_view.userhome, name = 'home'),
    path('registration/', user_view.signup2, name='manual-signup'),
    path('signup2/', user_view.signup2, name='signup2'),
    path('login2/', user_view.login2, name='login2'),
    path('base2/', user_view.basePage, name='base2'),
    path('profile/',user_view.profile, name='profile')
]
path('login/', user_view.login),
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)