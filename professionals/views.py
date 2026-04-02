from rest_framework.viewsets import ModelViewSet
from .models import Professional
from .serializers import ProfessionalSerializer


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer