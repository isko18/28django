from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from main.forms import ProductForm
from main.models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', locals())

class ProductCreateView(CreateView):
    template_name = 'create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("index")