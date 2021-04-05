from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path ('',views.sondershop, name ='sondershop'),
    path ('<int:shop_id>/',views.detail, name = 'detail'),
    ]
