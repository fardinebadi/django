from django.urls import path
from products.views import show_product,category,show_list_pro,welcome_page
urlpatterns = [
    
    path('showproduct/',show_product),
    path('category/',category),
    path('show_all_product/',show_list_pro),
    path('',welcome_page)
]