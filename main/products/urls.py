from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductView.as_view(), name='products'),
    path("create_review/", views.CreateReviewView.as_view(), name="create_review"),
    path("products/<int:id>/", views.ProductsDetailView.as_view(), name="products_detail"),
    path("category_product/", views.AddProductView.as_view(), name="category_product"),
    path("old_product/", views.OldView.as_view(), name="old_product"),
    path("new_product/", views.NewView.as_view(), name="new_product"),
]
