from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_oder/', views.processOder, name='process_oder'),  
]