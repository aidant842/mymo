from django.shortcuts import render


def index(request):
    """ A view to return the home """

    context = {
        'counter': 10,
    }

    template = 'home/index.html'
    return render(request, template, context)
