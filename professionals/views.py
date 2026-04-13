from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.utils.api_response import error_response, success_response

from .models import Professional
from .serializers import ProfessionalSerializer


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

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
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                success_response(serializer.data), status=status.HTTP_200_OK
            )

        return Response(
            error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST
        )

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(success_response(None), status=status.HTTP_204_NO_CONTENT)
