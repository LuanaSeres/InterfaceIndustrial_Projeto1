from django.urls import path
from contador import views

urlpatterns = [
    path('dados/', views.dados_list, name='dados-list'),
]
