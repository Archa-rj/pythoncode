
from .import views
from django.urls import path, include

from journeyproject import settings

urlpatterns = [
    path('register',views.registration,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]