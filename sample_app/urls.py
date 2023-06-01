from django.urls import path
from sample_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home_page',views.home_page,name='home_page'),
    path('sign_up',views.sign_up,name='sign_up'),


]