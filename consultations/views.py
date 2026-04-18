from rest_framework import status
from rest_framework.permissions import (
    SAFE_METHODS,
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.utils.api_response import error_response, success_response

from .models import Consultation
from .serializers import ConsultationSerializer


class ConsultationViewSet(ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]

        if self.request.method == "DELETE":
            return [IsAdminUser()]

        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                success_response(serializer.data), status=status.HTTP_201_CREATED
            )

        return Response(
            error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(success_response(serializer.data), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(success_response(serializer.data), status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instace = self.get_object()
        serializer = self.get_serializer(instace, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                success_response(serializer.data), status=status.HTTP_200_OK
            )

        return Response(
            error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        instace = self.get_object()
        self.perform_destroy(instace)

        return Response(success_response(None), status=status.HTTP_204_NO_CONTENT)
