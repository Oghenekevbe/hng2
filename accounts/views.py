from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .tokens import get_tokens_for_user
from main.models import Organisation,OrganizationMembership
from .models import User
from .serializers import UserSerializer, LoginSerializer
from services.errors import *
from services.status_messages import *

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = User.objects.create_user(
                    email=serializer.validated_data['email'],
                    password=request.data['password'],
                    firstName=serializer.validated_data['firstName'],
                    lastName=serializer.validated_data['lastName'],
                    phone=serializer.validated_data.get('phone', '')
                )
                org_name = f"{user.firstName}'s Organisation"
                organisation = Organisation.objects.create(name=org_name)
                OrganizationMembership.objects.create(user=user, organization=organisation)

                # Remove 'password' field from serializer.data
                serializer_data = serializer.data.copy()
                serializer_data.pop('password', None)

                refresh = get_tokens_for_user(user)
                response_data = {
                    'status': 'success',
                    'message': 'Registration successful',
                    'data': {
                        'accessToken': refresh['access'],
                        'user': serializer_data
                    }
                }
                return created_successfully(data=response_data)
            else:
                errors = get_error_messages(serializer)
                return generate_error_response(errors)

        except Exception as e:
            return generate_registration_error()
    
class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = get_tokens_for_user(user)
            serializer = self.serializer_class(user)
            response_data = {
                'status': 'success',
                'message': 'Login successful',
                'data': {
                    'accessToken': refresh['access'],
                    "user": {
                                "userId": user.userId,
                                "firstName": user.firstName,
                                        "lastName": user.lastName,
                                        "email": user.email,
                                        "phone": user.phone,
                            }
                }
            }
            return success_response(data=response_data)
        return  authentication_failed()
