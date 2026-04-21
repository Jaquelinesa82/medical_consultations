from rest_framework import serializers

from .models import Consultation


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"

    def validate(self, data):
        # pega valores do payload ou da instância (PATCH)
        date = data.get("date", getattr(self.instance, "date", None))
        time = data.get("time", getattr(self.instance, "time", None))

        if not date or not time:
            raise serializers.ValidationError("Data e horário são obrigatórios.")

        return data

    def validate_patient_name(self, value):
        print(value)
        return value.strip().title()
