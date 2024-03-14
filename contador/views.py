from django.shortcuts import render
from rest_framework import viewsets
from .models import Dados
from .serializers import DadosSerializer

class Screen(viewsets.ModelViewSet):
    queryset = Dados.objects.all()  
    serializer_class = DadosSerializer

    def list(self, request):
        last_entity = Dados.objects.last()
        return render(request, 'dados.html', {'contador': [last_entity]})