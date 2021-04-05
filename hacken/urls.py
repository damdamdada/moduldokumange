
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='hack'
urlpatterns = [
    path ('',views.hacken, name ='hacken'),
    path ('<int:hack_id>/',views.detailhack, name = 'detailhack'),
    ]
