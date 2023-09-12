from django.shortcuts import get_object_or_404
from .models import Person
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import PersonSerializer

# Create your views here.

class api(APIView):
    serializer_class = PersonSerializer

    def get(self, request, pk=None):
            name = request.query_params.get('name', '')
            age = request.query_params.get('age', '')
            if pk is not None:
                person = get_object_or_404(Person, pk=pk)
                serializer = self.serializer_class(person)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            elif age:
                persons = Person.objects.filter(age=age)
                serializer = self.serializer_class(persons, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            elif name:
                persons = Person.objects.filter(name=name)
                serializer = self.serializer_class(persons, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                persons = Person.objects.all()
                serializer = self.serializer_class(persons, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Person created successfully',
                'data': serializer.data
            }
            return Response(data=response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'error': 'Person not created'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if request.method == 'PUT':
            name = request.query_params.get('name', '')
            age = request.query_params.get('age', '')

            if pk is not None:
                persons = get_object_or_404(Person, name=name)
            elif name:
                persons = Person.objects.filter(name=name).first()
                if not persons:
                    return Response(data={'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
            elif age:
                persons = Person.objects.filter(age=age)
                if not age:
                    return Response(data={'error': 'Person with {age} not available'}, status=status.HTTP_404_NOT_FOUND)
                serializer = self.serializer_class(persons, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        
            data = request.data
            serializer = self.serializer_class(persons, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'message': 'Person instance updated successfully',
                    'data': serializer.data
                }
                return Response(data=response_data, status=status.HTTP_200_OK)
            else:
                return Response(data={'error': 'Invalid data for updating person'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        name = request.query_params.get('name', '')
        if pk is not None:
            persons = get_object_or_404(Person, name=name)
        elif name:
            persons = Person.objects.filter(name=name).first()
            if not persons:
                return Response(data={'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)


        persons.delete()
        return Response(data={'message': 'Person instance successfully deleted'}, status=status.HTTP_204_NO_CONTENT)




            



