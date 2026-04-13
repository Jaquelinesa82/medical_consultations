from rest_framework import serializers
from .models import Professional

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
    
    def validate_contact(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Contato inválido')
        return value
    
    def validate(self, data):
        social_name = data.get('social_name')
        occupation = data.get('occupation')
        address = data.get('address')

        # valida só se vier no payload
        if social_name is not None and not social_name.strip():
            raise serializers.ValidationError("Nome social não pode ser vazio")

        if address is not None and not address.strip():
            raise serializers.ValidationError("Endereço obrigatório.")

        if (
            social_name is not None and
            occupation is not None and
            social_name.strip() == occupation.strip()
        ):
            raise serializers.ValidationError(
                "Nome e ocupação não podem ser iguais."
            )

        return data
