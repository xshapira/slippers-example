from django.shortcuts import render


def index(request):
    context = {
        "hi": "qaq"
    }
    return render(request, 'index.html', context=context)
