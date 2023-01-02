from django.shortcuts import render, redirect
from .forms import PersonForm
# Create your views here.
from django.shortcuts import render
from .models import Person


def list_people(request):
 people = Person.objects.all()
 return render(request, 'mustafaapp/people_list.html', {'people':
people})

def index_page(request):
 return render(request, 'mustafaapp/index.html')

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_people')
    else:
        form = PersonForm()
    return render(request, 'mustafaapp/create_person.html', {'form':
form})

