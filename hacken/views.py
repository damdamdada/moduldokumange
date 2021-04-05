from django.shortcuts import render, get_object_or_404
from .models import Hack
# Create your views here.
def hacken(request):
    hacks = Hack.objects.all()
    return render(request, 'hacken/hacken.html',{'hacks':hacks})
def detailhack(request, hack_id):
    hack = get_object_or_404(Hack, pk=hack_id)
    return render (request, 'hacken/detailhack.html',{'hack':hack})
