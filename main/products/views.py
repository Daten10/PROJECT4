from django.shortcuts import render
from . import models, forms
from django.views import generic
from django.shortcuts import get_object_or_404


class ProductView(generic.ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'product'
    ordering = ['-id']
    model = models.Product

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class CreateReviewView(generic.CreateView):
    template_name = "create_review.html"
    form_class = forms.ReviewForm
    success_url = "/products/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


class ProductsDetailView(generic.DetailView):
    template_name = "product/product_detail.html"
    context_object_name = "product_id"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)


class AddProductView(generic.ListView):
    template_name = "product/category_product.html"
    context_object_name = "category_product"
    model = models.Product

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class OldView(generic.ListView):
    template_name = "product/old_product.html"
    context_object_name = "old_product"
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name="Пенсионеры").order_by("-id")


class NewView(generic.ListView):
    template_name = "product/new_product.html"
    context_object_name = "new_product"
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name="Молодежь").order_by("-id")
