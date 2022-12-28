from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('<slug:category>', views.home_view, name='home_view'),
]
