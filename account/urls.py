
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('bnak_account', views.bnak_account , name='bnak_account'),
    path('login/', views.login , name='login'),
    path('register/', views.register , name='register'),
    path('adminpage/', views.adminpage , name='adminpage'),
    path('student/', views.student , name='student'),
    path('techer/', views.techer , name='techer'),
]
