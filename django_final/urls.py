"""django_final URL Configuration

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
from django.contrib.auth import views as auth_views #django built-in login page
from django.urls import path, include
from users import views as us_view
# from django documentation
from django.conf import settings
from django.conf.urls.static import static
#URL comes here first. Path redirects to blog.urls
urlpatterns = [
    path('admin/', admin.site.urls), #admin page
    path('register/',us_view.register, name='register'), #register page
    path('profile/',us_view.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #login
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #logout - default page is django admin page
    path('', include('blog.urls')) # A function that takes a full Python import path to another URLconf module that should be “included” in this place.
]

if settings.DEBUG:
    urlpatterns+=(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))