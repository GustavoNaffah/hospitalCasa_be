from rest_framework import status, views
from rest_framework.response import Response
from hospitalApp.serializers.hClinicaSerializer import HisClinicaSerializer

class CrearHisClinicaView(views.APIView):
    def post(self, request):
        serializer = HisClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(HisClinicaSerializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 