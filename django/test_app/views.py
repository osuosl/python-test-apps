from django.http import HttpResponse


def index(request):
    return HttpResponse("Django app successfully installed")