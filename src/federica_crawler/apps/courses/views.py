from django.views import generic
from django.shortcuts import render
from .models import Course
from apps.crawler.run_crawler import collect_data


class IndexView(generic.ListView):
    template_name = 'course/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return all Courses."""
        return Course.objects.order_by('title')


class DetailView(generic.DetailView):
    model = Course
    template_name = 'course/detail.html'


def scrape(request):
    if(request.GET.get('scrapebtn')):
        collect_data()
    return render(request, 'course/scraping.html')