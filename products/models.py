from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    category = models.ManyToManyField(Category, verbose_name=_('category'), related_name='product_category')
    description = models.TextField(_('description'), max_length=10000)
    maximum_velocity = models.CharField(_('max_velocity'), max_length=100, blank=True, null=True)
    electrical_capacity = models.CharField(_('electrical_capacity'), max_length=100, blank=True, null=True)
    length = models.CharField(_('length'), max_length=20, blank=True, null=True)
    width = models.CharField(_('width'), max_length=20, blank=True, null=True)
    height = models.CharField(_('height'), max_length=20, blank=True, null=True)
    diameter = models.CharField(_('diameter'), max_length=20, blank=True, null=True)
    size = models.CharField(_('size'), max_length=20, blank=True, null=True)
    weight = models.CharField(_('weight'), max_length=20, blank=True, null=True)
    production_capacity = models.CharField(_('production_capacity'), max_length=100, blank=True, null=True)
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=8, blank=True, null=True)
    code = models.CharField(_('code'), max_length=8, unique=True)
    image = models.ImageField(_('image'), upload_to='products/', blank=True, null=True)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='product_images',
                                on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='products/')
