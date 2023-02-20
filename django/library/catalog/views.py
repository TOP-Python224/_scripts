from django.shortcuts import render

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

