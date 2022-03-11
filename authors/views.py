from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):

    registes_form_data = request.session.get('registes_form_data', None)

    form = RegisterForm(registes_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['registes_form_data'] = POST

    form = RegisterForm(POST)

    return redirect('authors:register')
