from django.views import generic
from django.template.response import TemplateResponse
from .models import Course
from apps.crawler.run_crawler import collect_data


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return all Courses."""
        return Course.objects.order_by('title')


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'


def buttons(request):
    """Return a ButtonAction instance that manage all the various buttons"""
    return ButtonActions(request)


class ButtonActions(TemplateResponse):
    """Read which button has been clicked from the response and execute the required actions rendering the right template"""

    def scrape(self):
        """Call scrapy crawler to load data in the db"""
        collect_data()
        self.template_name = 'courses/actions/scrape.html'

    def delete(self):
        """Delete all courses from the db"""
        Course.objects.all().delete()
        self.template_name = 'courses/actions/delete.html'

    def __init__(self, request):
        self.request = request
        if(self.request.GET.get('scrape')):
            self.scrape()
        if(self.request.GET.get('delete')):
            self.delete()
        super().__init__(request, self.template_name)
