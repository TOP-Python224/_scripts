from django.views.generic import ListView, DetailView

from structure.models import Faculty


class IndexView(ListView):
    model = Faculty
    template_name = 'structure/index.html'


class FacultyView(DetailView):
    model = Faculty
    template_name = 'structure/faculty.html'

    def get_context_data(self, **kwargs):
        return {
            'page_title': self.object.acronym.upper()
        } | super().get_context_data(**kwargs)

