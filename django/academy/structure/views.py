from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from structure.forms import AddDepartment
from structure.models import Faculty


# faculty_menu = {
#     faculty.acronym: [
#         {'name': 'Head', 'url': f'/{faculty.acronym}/head/'},
#         {'name': 'Departments', 'url': f'/{faculty.acronym}/departments/'},
#         {'name': 'Science', 'url': f'/{faculty.acronym}/science/'},
#     ]
#     for faculty in Faculty.objects.all()
# }

# department_menu = (
#     {'name': 'Head', 'url': 'head/'},
#     {'name': 'Teachers', 'url': 'teachers/'},
#     {'name': 'Groups', 'url': 'groups/'},
#     {'name': 'Programs', 'url': 'programs/'},
# )


class IndexView(ListView):
    model = Faculty
    template_name = 'structure/index.html'


class FacultyView(View):

    def get(self, request, *args, **kwargs):
        view = FacultyDetails.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = FacultyAddDepartment.as_view()
        return view(request, *args, **kwargs)


class FacultyDetails(DetailView):
    model = Faculty
    template_name = 'structure/faculty.html'

    def get_context_data(self, **kwargs):
        return {
            'page_title': self.object.acronym.upper(),
            'form': AddDepartment(),
            # 'top_menu': faculty_menu[self.object.acronym],
        } | super().get_context_data(**kwargs)


class FacultyAddDepartment(SingleObjectMixin, FormView):
    model = Faculty
    form_class = AddDepartment
    template_name = 'structure/faculty.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save_with_fk(self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(self.object.acronym, kwargs={'pk': self.object.pk})

