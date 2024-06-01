from django.urls import path
from . import views

urlpatterns = [
    path('main_page/', views.MainPageView.as_view(), name='main_page'),
]
