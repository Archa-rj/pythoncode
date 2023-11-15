from django.urls import path
from . import views

app_name='credentials'
urlpatterns = [

     path('register',views.sign_up,name='register'),
    path('login',views.sign_in,name='login'),
    # path('new',views.login,name='new'),
    path('form',views.form,name='form'),
    path('submit',views.submit,name='submit'),
path('logout',views.logout_user,name='logout'),
    path('dir_form',views.dir_form,name='dir_form'),

    path('add',views.person_create_view,name='person_add'),
    path('<int:pk>/',views.person_update_view,name='person_change'),
    path('ajax/load-office/',views.load_cities,name='ajax_load_office'),



# path('add/', views.person_create_view, name='person_add'),
#     path('<int:pk>/', views.person_update_view, name='person_change'),
#
#
#     path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX


]
