from django.urls import path
from main.views import index, ProductCreateView

urlpatterns = [
    path('', index, name='index'),
    path("create/", ProductCreateView.as_view(), name='create')
]
