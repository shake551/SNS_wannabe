from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend

def index(request):
    params = {
        'title': 'Hello',
        'message': 'all friends. ',
        'form': HelloForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)