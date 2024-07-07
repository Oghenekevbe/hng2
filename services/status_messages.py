# service.py
from rest_framework.response import Response
from rest_framework import status

def created_successfully(data, status_code=status.HTTP_201_CREATED):
    return Response(data, status=status_code)


def success_response(data, status_code=status.HTTP_200_OK):
    return Response(data, status=status_code)
