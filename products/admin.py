from django.contrib import admin
from .models import Category, Product, ProductImages

# Register your models here.

admin.site.register(Category)


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin, ]
    list_display = ('name', 'code')
    list_filter = ('price',)
    search_fields = ('name', 'code')


admin.site.register(Product, ProductAdmin)
