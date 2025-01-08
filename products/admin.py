from django.contrib import admin
from products.models import Product,Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=["name_product","product_price"]




class CatgoryeAdmin(admin.ModelAdmin):
    list_display=["name_category"]
   

        
        
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CatgoryeAdmin)