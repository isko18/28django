import django_filters
from main.models import Product

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Название")
    price__gte = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label="Цена от")
    price__lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Цена до")
    
    class Meta:
        model = Product
        fields = ['title', 'price__gte', 'price__lte']