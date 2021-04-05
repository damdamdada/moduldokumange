from django.shortcuts import render
from .models import Work
# Create your views here.
def workshop (request):
    works = Work.objects.all()
    return render (request, 'workshop/workshop.html',{'works':works})
