from django.shortcuts import render


def index(request):
    """ A view to return the home """

    template = 'home/index.html'
    return render(request, template)
