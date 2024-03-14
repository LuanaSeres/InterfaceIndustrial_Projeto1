from django.shortcuts import render
from contador.models import Dados
from rest_framework import viewsets
from contador.serializers import DadosSerializer

class Screen(viewsets.ModelViewSet):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

    def list(self, request, *args, **kwargs):
        last_entity = Dados.objects.last()  
        return render(request, 'ultimos_dados.html', {'count':[last_entity]})