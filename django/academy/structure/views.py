from django.views.generic import ListView, DetailView

from structure.models import Faculty


class IndexView(ListView):
    model = Faculty
    template_name = 'structure/index.html'


class FacultyView(DetailView):
    model = Faculty
    template_name = 'structure/faculty.html'

