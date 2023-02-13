from django.http.response import HttpResponse


def index_view(request):
    return HttpResponse(
        '<h1>First Django Project</h1>'
        '<p>Hello World</p>'
    )

