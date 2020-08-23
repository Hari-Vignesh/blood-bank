from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.forms import ModelForm

from .models import Person
from .forms import PersonForm
from .utils import blood_relationships, get_age, get_bmi, paginate


def people_list(request):
    people = Person.objects.all().order_by('-id')
    people = paginate(request, people, 10)
    context = {
        'people': people,
    }
    return render(request,
        'relations/people_list.html',
        context=context
    )

def people_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except:
        raise Http404("Person does not exist")
    age = get_age(person.dob)
    context = {
        'person': person,
        'age' : age,
        'bmi': get_bmi(person.height, person.weight),
    }
    return render(request,
        'relations/people_detail.html',
        context=context
    )

def people_receives(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except:
        raise Http404("Person does not exist")
    people = Person.objects.filter(blood_type__in=blood_relationships[person.blood_type]["receives"]).exclude(pk=person.id)
    context = {
        'person': person,
        'people': people,
    }
    return render(request,
        'relations/people_receives.html',
        context=context
    )

def people_gives(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except:
        raise Http404("Person does not exist")
    people = Person.objects.filter(blood_type__in=blood_relationships[person.blood_type]["gives"]).exclude(pk=person.id)
    context = {
        'person': person,
        'people': people,
    }
    return render(request,
        'relations/people_gives.html',
        context=context
    )


def add_person(request): 
    form = PersonForm(request.POST or None) 
    if form.is_valid():
        cd = form.cleaned_data
        person = Person(**cd)
        person.save()
        return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request,
        "relations/add_person.html",
        context
    ) 
