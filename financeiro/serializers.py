from rest_framework import serializers
from .models import Transacao

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = "__all__"
        read_only_fields = ('usuario',)

    def validate_valor(self, value):
            if value < 0:
                raise serializers.ValidationError("Não utilize números negativos")
            return value
    
    def validate(self, data):
        descricao = data.get("descricao", "").lower()
        tipo = data.get("tipo_de_transacao", "")
        if "salário" in descricao and tipo == 'SAÍDA':
             raise serializers.ValidationError("salário não é uma saída")
        return data