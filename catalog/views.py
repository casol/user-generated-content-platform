from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Content
from .forms import ContentForm


def home(request):
    content = Content.objects.all()
    return render(request,
                  'catalog/tmp/home.html',
                  {'content': content})


def content_detail(request, custom_url):
    obj = get_object_or_404(Content, custom_url=custom_url)
    return render(request,
                  'catalog/tmp/detail.html',
                  {"content": obj})


@login_required
def content_upload(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    else:
        form = ContentForm()
    return render(request, 'catalog/tmp/upload.html', {
        'form': form
    })


def test(request):
    return render(request,
                  'catalog/test.html')
