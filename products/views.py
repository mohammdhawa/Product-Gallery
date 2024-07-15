from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.views.generic import ListView, DetailView


# Create your views here.
def get_first_word(s):
    return s.split()[0]

def home(request):

    return render(request, 'products/home.html', {})


class ProductListView(ListView):
    model = Product
    template_name = 'products/home.html'

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset[:8]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

