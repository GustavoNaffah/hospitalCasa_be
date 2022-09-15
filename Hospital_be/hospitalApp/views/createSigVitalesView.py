from rest_framework import status, views
from rest_framework.response import Response
from hospitalApp.serializers.sigVitalesSerializer import SigVitalesSerializer

class CrearSigVitalesView(views.APIView):
    def post(self, request):
        serializer = SigVitalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(SigVitalesSerializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 