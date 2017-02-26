from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature, Value, FeatureValue

# Create your views here.
def index(request):
    print('работает views.py')
    for f in Feature.objects.all():
        print(f, ':')
        for fv in FeatureValue.objects.filter(feature=f):
            print('   ', fv.value)
    print('--------------')
    for fv in FeatureValue.objects.filter(value__has__icontains = 'r'):
        print(fv.feature, ' : ', fv.value)
    print('конец  views.py')

    return HttpResponse('<h1>stuff.views.index</h1>')