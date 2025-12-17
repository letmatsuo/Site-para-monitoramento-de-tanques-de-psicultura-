from django.urls import path 
from . import views
from .views import LeituraAmonia
 

urlpatterns =[
  #  path('', views.all_user)
  path("api/dados/", views.api_dados, name="api_dados"),
  path('leitura/', views.mostrar_leitura, name='mostrar_leitura'),
  path('', views.index, name='index'),
  path('amonia/', views.amonia_view, name='amonia'),
    path('amonia/', views.amonia, name='amonia'),
    path('ph/', views.ph, name='ph'),
    path('oxigenio/', views.oxigenio, name='oxigenio'),
    path('temperatura/', views.temperatura, name='temperatura'),
    path('turbidez/', views.turbidez, name='turbidez'),
    path('inicio/', views.inicio, name='inicio'),
  #path('oxigenio/', views.amonia_view, name='amonia'),

 # path('api/receber-amonia/', views.receber_amonia, name='receber_amonia'),
  #path('api/amonia/', LeituraAmonia.as_view()),   # path('amonia/', views.amonia_view, name='amonia'),
 #  path('peixonauta/',views.ok)
]