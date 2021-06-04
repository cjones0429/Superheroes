from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name,
                                  alter_ego=alter_ego,
                                  primary_ability=primary_ability,
                                  secondary_ability=secondary_ability,
                                  catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, superhero_id):
    superhero = Superhero.objects.get(id=superhero_id)
    if request.method == 'POST':
        superhero.name = request.POST.get('name')
        superhero.alter_ego = request.POST.get('alter_ego')
        superhero.primary_ability = request.POST.get('primary_ability')
        superhero.secondary_ability = request.POST.get('secondary_ability')
        superhero.catchphrase = request.POST.get('catchphrase')
        superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
            'superhero': superhero
        }
        return render(request, 'superheroes/edit.html', context)


def delete(request, superhero_id):
    superhero = Superhero.objects.get(id=superhero_id)
    superhero.delete()
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    superhero = Superhero.objects.get(id=superhero_id)
    context = {
        'superhero': superhero
    }
    return render(request, 'superheroes/details.html', context)


