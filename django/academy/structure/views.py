from django.views.generic import ListView

from structure.models import Faculty


class IndexView(ListView):
    model = Faculty
    template_name = 'structure/index.html'

