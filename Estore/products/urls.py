from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('<slug:category>', views.home_view, name='home_view'),
    path('search/', views.product_search_view, name='product_search_view'),
    path('detail/<slug:cat>/<slug:prd>/', views.product_detail_view, name='product_detail_view')
]
