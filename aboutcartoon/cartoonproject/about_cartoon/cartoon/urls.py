from . import views
from django.urls import path
app_name='cartoon'
urlpatterns = [

    path('',views.index,name='index'),
    path('cartoon/<int:c_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
