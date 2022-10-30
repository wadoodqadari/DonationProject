

from django.contrib import admin

from .models import *

# Register your models here.

class PurchaseImageAdmin(admin.StackedInline):
    model = PurchaseImage
    extra = 1




class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseImageAdmin]
 
    class Meta:
       model = Purchase
   


admin.site.register(Category)
admin.site.register(PurchaseImage)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sell)