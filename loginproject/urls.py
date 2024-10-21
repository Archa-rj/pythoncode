"""
URL configuration for loginproject project.

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
from django.urls import path,include
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('register',views.registration,name='register'),
    path('about',views.about,name='about'),
    path('display',views.display,name='display'),
    # path('signup/',views.signup_page,name='signup_form'),
    # path('contact/',include('contact.urls')),
    # path('products/',include('productsapp.urls')),
    # path('pagevisit/',views.pagevisit,name='page_visit'),
    # path('login/',views.login_page,name='login'),
    # path('logout/',views.logout_view,name='logout')
   
   
    
 
    
]
