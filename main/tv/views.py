from django.shortcuts import render
from . import models
from django.views import generic


class MainPageView(generic.ListView):
    template_name = 'main_page.html'
    context_object_name = 'main'
    ordering = ['-id']
    model = models.Slogan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Slogan'] = models.Slogan.objects.order_by('-id')
        context['TopGadgets'] = models.TopGadgets.objects.order_by('-id')
        context['Video'] = models.Video.objects.order_by('-id')
        return context

