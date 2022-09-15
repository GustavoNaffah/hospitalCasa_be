from rest_framework import status, views
from rest_framework.response import Response
from hospitalApp.serializers.pSaludSerializer import PerSaludSerializer

class CrearPSaludView(views.APIView):
    def post(self, request):
        serializer = PerSaludSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response(PerSaludSerializer.validated_data, status=status.HTTP_201_CREATED)