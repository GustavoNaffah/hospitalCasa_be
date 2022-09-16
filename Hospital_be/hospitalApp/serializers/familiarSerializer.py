from pyexpat import model
from hospitalApp.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields=['iduser','idPaciente','parentesco','correo']