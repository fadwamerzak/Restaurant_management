from django.urls import path 
from .views import (aliment_list , per_product_view ,add_aliment,delete_aliment,update_aliment)
urlpatterns = [
    path('',aliment_list, name='aliment_list'),
    path('per_product/<int:pk>',per_product_view, name='per_product'),
    path('add_aliment/',add_aliment, name='add_aliment'),
    path('delete/<int:pk>',delete_aliment, name='delete_aliment'),
    path('update/<int:pk>',update_aliment, name='update_aliment'),
]