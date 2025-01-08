from django.shortcuts import render
from products.models import Product,Category

# Create your views here.
def welcome_page(request):
    return render(request,'welcome.html')

def show_product(request):
    info=Product.objects.all()
    return render(request,'product.html',{'info':info})
def category(request):
    info_cat=Product.objects.get(id=1)
    cate=info_cat.category_at.all()
    return render(request,'catgory.html',{'info_cat':info_cat,"cate":cate})
def show_list_pro(request):
    info_list=Product.objects.all()
    return render(request,'list_product.html',{'info_list':info_list})
