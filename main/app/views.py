from django.shortcuts import render, HttpResponse
from .forms import *


def index(request):
    return render(request, 'app/index.html', {'form': One_form})


def task_2(request):
    context = {}
    message = False
    if request.method == 'POST':
        form = Two_form(request.POST)
        if form.is_valid():
            context['Name'] = form.cleaned_data['Name']
            context['Suname'] = form.cleaned_data['SuName']
            context['Email'] = form.cleaned_data['Email']
            context['Adress'] = form.cleaned_data['Adress']
        message = True


    else:
        form = Two_form()

    context['form'] = form
    context['message'] = message
    return render(request, 'app/task_2.html', context)


def appointment(request):
    form = One_form(request.POST)
    print(form.__dict__['data'])
    Name = form.__dict__['data'].get('Name', 'Имя')
    Phone = form.__dict__['data'].get('Phone', 'Телефон')
    Email = form.__dict__['data'].get('Email', 'Почта')
    TextArea = form.__dict__['data'].get('TextArea', 'ТекстЭрия')
    Select  = form.__dict__['data'].get('Select', 'Слелект')
    return HttpResponse(f'''
        <p>Name: {Name}</p>
        <p>Phone: {Phone}</p>
        <p>Email: {Email}</p>
        <p>TextArea: {TextArea}</p>
        <p>Select: {Select}</p>
    ''')
