from django.views.generic import DetailView, ListView

from .models import Product


class CategoryFilteredMixin:
    def get_queryset(self, *args, **kwargs):
        parent_page = self.kwargs['parent_page']

        qs = super().get_queryset(*args, **kwargs)
        if parent_page.category:
            return qs.filter(category=parent_page.category)
        return qs


class ProductList(CategoryFilteredMixin, ListView):
    model = Product


class ProductDetail(CategoryFilteredMixin, DetailView):
    model = Product
