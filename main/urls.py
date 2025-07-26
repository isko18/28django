from django.urls import path
from main.views import index, product_detail, live_search, ProductCreateView

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path("create/", ProductCreateView.as_view(), name='create'),
    path("live_search/", live_search, name='live_search')
]
