from django.shortcuts import render, redirect
from django.urls import reverse

from catalog.forms import MyForm
from catalog.models import Author, Publisher


def index(request):
    return render(
        request,
        'catalog/index.html',
        {
            'authors_list': Author.objects.all(),
            'publishers_list': Publisher.objects.all(),
        }
    )


def publisher(request, pub_id: int):
    publisher = Publisher.objects.get(pk=pub_id)
    return render(
        request,
        'catalog/publisher.html',
        {
            'page_title': publisher.name,
            'publisher': publisher,
        }
    )


def contacts(request):
    return render(
        request,
        'catalog/contacts.html',
    )


def my_form_view(request):
    if request.method == 'GET':
        form = MyForm()

    elif request.method == 'POST':
        form = MyForm(request.POST)
        print(f'{form.data = }')
        if form.is_valid():
            print(f'{form.cleaned_data = }')
            return redirect(reverse('main'))

    return render(
        request,
        'structure/forms_test.html',
        {
            'form': form,
        }
    )


# class MyFormView(FormView):
#     form_class = MyForm
#     template_name = 'structure/forms_test.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         print(f'{form.cleaned_data}')
#         return super().form_valid(form)

