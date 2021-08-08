from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import data


class HomePageView(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = data.objects.all()
        return context


class SearchResultsView(ListView):
    model = data
    template_name = 'search/search_results.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = data.objects.filter(
            Q(chapter_name__icontains=query) | Q(section__icontains=query) | Q(section_name__icontains=query) | Q(description__icontains=query)
        )
        return object_list
