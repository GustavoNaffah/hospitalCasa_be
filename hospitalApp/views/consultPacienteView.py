from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from hospitalApp.models.paciente import Paciente
from hospitalApp.serializers.pacienteSerializer import PacienteSerializer
class ConsultPacienteView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)
        