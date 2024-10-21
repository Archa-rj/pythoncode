from django.urls import path
from .import views

urlpatterns = [
    path('',views.contact,name='contact'),
    path('contactus',views.contact_us,name='contactus')
]