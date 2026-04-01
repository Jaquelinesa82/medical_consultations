from rest_framework import serializers
from .models import Professionals


class ProfessionalsSerializer(serializers.ModelSerializer):
    class meta:
        model = Professionals
        fields = '__all__'