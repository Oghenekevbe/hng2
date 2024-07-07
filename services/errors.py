from rest_framework import status
from rest_framework.response import Response

def get_error_messages(serializer):
    """
    Retrieves error messages from serializer errors and returns a list of dictionaries.
    Each dictionary contains 'field' and 'message'.
    """
    errors = []
    for field, messages in serializer.errors.items():
        for message in messages:
            errors.append({
                'field': field,
                'message': message
            })
    return errors

def generate_error_response(errors, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY):
    """
    Generates a standard error response format for validation errors.
    'errors' should be a list of dictionaries, each containing 'field' and 'message'.
    """
    return Response({'errors': errors}, status=status_code)


def generate_registration_error():
    """
    Generates a specific error response for unsuccessful registration.
    """
    return Response({
        'status': 'Bad request',
        'message': 'Registration unsuccessful',
        'statusCode': status.HTTP_400_BAD_REQUEST
    }, status=status.HTTP_400_BAD_REQUEST)

def client_error():
    """
    Generates a specific error response for unsuccessful organisation creation.
    """
    return Response({
        'status': 'Bad request',
        'message': 'Client error',
        'statusCode': status.HTTP_400_BAD_REQUEST
    }, status=status.HTTP_400_BAD_REQUEST)



def authentication_failed():
    """
    Generateserror response for unsuccessful login.
    """
    return Response({'status': 'Bad request', 'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)