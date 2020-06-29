from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from ports.list_ports import serial_ports


class PortsAPIView(APIView):

    def get(self, request):
        ports = serial_ports()
        if ports:
            return Response(data=ports, status=200)
        raise NotFound
