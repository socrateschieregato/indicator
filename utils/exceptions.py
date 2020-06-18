from rest_framework import status
from rest_framework.exceptions import APIException


class SerialNotFound(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Error - trying to conect, could not open port'

