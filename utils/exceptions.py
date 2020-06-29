from rest_framework import status
from rest_framework.exceptions import APIException


class SerialNotFound(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Error - trying to conect or could not open port'


class ReadSerialError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Error - get data from serial port'
