from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.product_create,name='createproduct'),
        path('read',views.product_read,name='read'),
        path('update/<int:pk>/',views.product_update,name='update'),
        path('delete/<int:pk>',views.product_delete,name='delete'),
        path('listing',views.listing,name='page_list')
    ]