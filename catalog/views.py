from django.shortcuts import render

from .models import Content


def index(request):
    content = Content.objects.all()
    return render(request,
                  'catalog/index.html',
                  {'content': content})
