
# Register your models here.
from django.contrib import admin
from .models import Product,Category



class CategoryAdmin(admin.ModelAdmin):
  list=('name')
admin.site.register(Category, CategoryAdmin)

# class TodoAdmin(admin.ModelAdmin):
#   list = ('title', 'description', 'completed')
# admin.site.register(Todo,TodoAdmin)
  
  