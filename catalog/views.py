from django.shortcuts import render, get_object_or_404

from .models import Content


def index(request):
    content = Content.objects.all()
    return render(request,
                  'catalog/index.html',
                  {'content': content})


def content_detail(request, pk):
    obj = get_object_or_404(Content, id=pk)
    return render(request,
                  'catalog/content_detail.html',
                  {"content": obj})