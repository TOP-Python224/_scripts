from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView

from structure.forms import MyForm
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


class FacultyView(DetailView):
    model = Faculty
    template_name = 'structure/faculty.html'

    def get_context_data(self, **kwargs):
        return {
            'page_title': self.object.acronym.upper(),
            # 'top_menu': faculty_menu[self.object.acronym],
        } | super().get_context_data(**kwargs)


class MyFormView(FormView):
    form_class = MyForm
    template_name = 'structure/forms_test.html'
    success_url = '/'

    def form_valid(self, form):
        print(f'{form.cleaned_data}')
        return super().form_valid(form)

