from django.shortcuts import render
from rest_framework import viewsets
from .models import Transacao
from .serializers import TransacaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class TransacaoViewSet(viewsets.ModelViewSet):
    serializer_class = TransacaoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo_de_transacao', 'data']
    
    def get_queryset(self):
        return Transacao.objects.filter(usuario = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario = self.request.user)

    @action(detail=False, methods=['GET'])
    def resumo(self, request):
        entradas_dict = Transacao.objects.filter(usuario = request.user, tipo_de_transacao = 'ENTRADA').aggregate(total = Sum('valor'))
        entradas = entradas_dict.get('total') or 0
        saidas_dict = Transacao.objects.filter(usuario = request.user, tipo_de_transacao = 'SAÍDA').aggregate(total = Sum('valor'))
        saidas = saidas_dict.get('total') or 0
        
        return Response({
            "entradas": entradas,
            "saidas": saidas,
            "saldo_total": entradas - saidas
        })


# Create your views here.
