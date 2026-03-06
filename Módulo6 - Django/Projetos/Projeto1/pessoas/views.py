from django.shortcuts import render
from datetime import date
from .models import Pessoa
#from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Olá Django!")
    p = Pessoa.objects.get(id=1)
    contexto = {"pessoas": p}
    return render(request, 'home.html', contexto)
