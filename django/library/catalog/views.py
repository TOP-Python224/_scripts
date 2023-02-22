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

