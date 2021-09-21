from django.views import generic
from .models import Course


class IndexView(generic.ListView):
    template_name = 'course/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return all Courses."""
        return Course.objects.order_by('title')


class DetailView(generic.DetailView):
    model = Course
    template_name = 'course/detail.html'