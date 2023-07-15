from django.shortcuts import render
from me.models import Me
# Create your views here.
def index(request):
    me = Me.objects.all()
    context = {
        'people':me
    }
    return render(request, 'index.html', context)

def second(request):
    return render(request, 'second.html')