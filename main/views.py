from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string

from main.forms import ProductForm
from main.models import Product
from main.filters import ProductFilter

# Create your views here.
def index(request):
    product = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product)
    return render(request, 'index.html', locals())

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', locals())

class ProductCreateView(CreateView):
    template_name = 'create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("index")
    
def live_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query) if query else Product.objects.all()
    html = render_to_string('product_cards.html', {'products': products})
    return JsonResponse({'html': html})