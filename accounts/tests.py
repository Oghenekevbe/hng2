from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from main.models import *

User = get_user_model()

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            "email": "testuser@example.com",
            "password": "testpassword123",
            "firstName": "John",
            "lastName": "Doe",
            "phone": "1234567890"
        }

    def test_register_user_successfully(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('accessToken', response.data['data'])
        self.assertEqual(response.data['data']['user']['email'], self.user_data['email'])

    def test_register_user_with_default_organisation(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('accessToken', response.data['data'])
        self.assertEqual(response.data['data']['user']['email'], self.user_data['email'])

        # Check if the default organisation was created
        user = User.objects.get(email=self.user_data['email'])
        default_org_name = f"{self.user_data['firstName']}'s Organisation"
        organisation = Organisation.objects.filter(name=default_org_name).first()
        self.assertIsNotNone(organisation)
        self.assertEqual(organisation.name, default_org_name)

        # Check if the user is part of the default organisation
        membership = OrganizationMembership.objects.filter(user=user, organization=organisation).first()
        self.assertIsNotNone(membership)


    def test_login_user_successfully(self):
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {
            "email": self.user_data['email'],
            "password": self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('accessToken', response.data['data'])

    def test_register_user_missing_fields(self):
        invalid_data = self.user_data.copy()
        invalid_data.pop('email')
        response = self.client.post(self.register_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_register_user_duplicate_email(self):
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_token_contains_user_details(self):
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {
            "email": self.user_data['email'],
            "password": self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        access_token = response.data['data']['accessToken']
        decoded_token = AccessToken(access_token)  
        self.assertEqual(decoded_token['email'], self.user_data['email'])
        self.assertEqual(decoded_token['firstName'], self.user_data['firstName'])
        self.assertEqual(decoded_token['lastName'], self.user_data['lastName'])
        self.assertEqual(decoded_token['phone'], self.user_data['phone'])    
        
    def authenticate_user(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        token = response.data['data']['accessToken']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        return response.data['data']['user']
