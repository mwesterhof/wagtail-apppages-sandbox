from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page

from app_pages.models import AppPageMixin


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductsPage(AppPageMixin, Page):
    url_config = 'products.urls'

    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)

    settings_panels = Page.settings_panels + [
        FieldPanel('category'),
    ]
