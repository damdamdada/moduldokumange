from django.shortcuts import render, get_object_or_404
from .models import Shop
# Create your views here.
def sondershop(request):
    shops = Shop.objects.all()
    return render(request,'sondershop/sondershop.html',{'shops':shops})
def detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render (request, 'sondershop/detail.html',{'shop':shop})
