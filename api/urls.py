from django.urls import path
from api.views import *

urlpatterns=[
    path('products/',get_products),
]
