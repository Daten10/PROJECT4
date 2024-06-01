from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductView.as_view(), name='products'),
    path("create_review/", views.CreateReviewView.as_view(), name="create_review"),
    path("products/<int:id>/", views.ProductsDetailView.as_view(), name="products_detail"),
]
