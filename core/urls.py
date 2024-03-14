from django.urls import path
from contador.views import receber_dados

urlpatterns = [
    path('api/receber_dados/', receber_dados, name='receber_dados'),
]
