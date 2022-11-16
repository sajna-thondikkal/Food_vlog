from . import views
from django.urls import path

urlpatterns=[
    path('register',views.register,name='register'),
    path('login_logout',views.login_logout,name='login_logout'),
    ]
