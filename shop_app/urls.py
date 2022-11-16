
from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prod_details,name='details'),
    path('search',views.searching,name='search')
]