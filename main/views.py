from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Organisation, OrganizationMembership
from .serializers import OrganisationSerializer,OrganizationMembershipSerializer
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from services.status_messages import *
from services.errors import *
import uuid


User = get_user_model()

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, uuid_str=None, *args, **kwargs):
        logged_in_user = request.user

        if uuid_str is None:
            return Response({'message' :'User identifier not provided'}, status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the user by userId
            user = User.objects.get(userId=uuid.UUID(uuid_str))

            # Check if the logged-in user has access to view the user's details
            if not user_in_organization(logged_in_user, user):
                return Response({'message' :'You do not have permission to view this user'}, status.HTTP_403_FORBIDDEN)

            # Serialize user data
            serializer = self.serializer_class(user)

            # Prepare response data
            response_data = {
                'status': 'success',
                'message': 'User Retrieval Successful',
                'data': {
                    "user": {
                        "userId": serializer.data['userId'],
                        "firstName": serializer.data["firstName"],
                        "lastName": serializer.data["lastName"],
                        "email": serializer.data["email"],
                        "phone": serializer.data["phone"],
                    }
                }
            }
            return success_response(data=response_data)

        except (User.DoesNotExist, ValueError):
            return Response({'message' :'User not found'}, status.HTTP_404_NOT_FOUND)
        

def user_in_organization(logged_in_user, user):
    """
    Checks if the logged-in user has access to view the details of the specified user.
    Checks if the specified user belongs to any organization that the logged-in user belongs to or has created.
    """
    # Retrieve organizations that the logged-in user belongs to or has created
    user_organizations = Organisation.objects.filter(member_orgs__user=logged_in_user)

    # Check if the specified user is a member of any of these organizations
    user_in_org = user_organizations.filter(member_orgs__user=user).exists()

    return user_in_org 



class UserOrganisationsView(generics.ListCreateAPIView):
    serializer_class = OrganizationMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return OrganizationMembership.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        # Extract only the values from the serializer data
        organisations_data = [
            {
                'orgId': item['orgId'],
                'name': item['name'],
                'description': item['description']
            }
            for item in serializer.data
        ]

        response_data = {
            'status': 'success',
            'message': 'Organisations Retrieved Successfully',
            'data': {
                'organisations': organisations_data
            }
        }
        return success_response(data=response_data)
    
    def post(self, request, *args, **kwargs):
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            organisation = Organisation(name=serializer.validated_data['name'],
                                        description=serializer.validated_data.get('description', ''))
            organisation.save()
            OrganizationMembership.objects.create(user=request.user, organization=organisation)
            response_data = {
                'status': 'success',
                'message': 'Organisation created successfully',
                'data': {
                    'orgId': str(organisation.orgId),
                    'name': organisation.name,
                    'description': organisation.description
                }
            }
            return created_successfully(data=response_data)
        return client_error()




class OrganisationDetailView(generics.RetrieveAPIView):
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,uuid_str,*args, **kwargs):
        org = Organisation.objects.get(orgId=uuid.UUID(uuid_str))
        serializer = self.serializer_class(org)
        response_data = {
                        "status": "success",
                            "message": "Organisation Successfully retrieved",
                        "data": {
                                "orgId": serializer.data['orgId'], 
                                "name":  serializer.data['name'], 
                                "description":  serializer.data['description']
                        }
                    }
        return success_response(data=response_data)


    
    



class AddUserToOrganisationView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, orgId):
        user_id = request.data.get('userId')

        if not user_id:
            return Response({"message" :"No userId provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(userId=user_id)
        except User.DoesNotExist:
            return Response({"message" :"User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            organisation = Organisation.objects.get(orgId=orgId)
        except Organisation.DoesNotExist:
            return Response({"message" :"Organisation does not exist"}, status=status.HTTP_404_NOT_FOUND)

        organization_membership, created = OrganizationMembership.objects.get_or_create(user=user, organization=organisation)

        if created:
            response_data = {'status': 'success', 'message': 'User added to organisation successfully'}
            return success_response(data=response_data)
        
        return Response({"message" :'User already in organisation'}, status=status.HTTP_400_BAD_REQUEST)
    




