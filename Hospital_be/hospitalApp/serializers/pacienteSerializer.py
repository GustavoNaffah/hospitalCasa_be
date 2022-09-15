from pyexpat import model
from hospitalApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=('perSalud','iduser','direccion','ciudad','fNacimiento')