from django.urls import path
from . import views
app_name='credentials'
urlpatterns = [

     path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    # path('new',views.login,name='new'),
    path('form',views.form,name='form'),
    path('submit',views.submit,name='submit'),


# path('add/', views.person_create_view, name='person_add'),
#     path('<int:pk>/', views.person_update_view, name='person_change'),
#
#
#     path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

     path('logout',views.logout,name='logout')
]
