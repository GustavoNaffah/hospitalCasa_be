from pyexpat import model
from hospitalApp.models.pSalud import PersonalSalud
from rest_framework import serializers

class PerSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalSalud
        fields=('iduser','rol','especialidad')