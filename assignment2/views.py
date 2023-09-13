from django.shortcuts import get_object_or_404
from .models import Person
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import PersonSerializer

# Create your views here.

class api(APIView):
    serializer_class = PersonSerializer

    def get(self, request, pk=None, name = None):
            if pk is not None:
                persons = get_object_or_404(Person, pk=pk)
                serializer = self.serializer_class(persons)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            elif name is not None:
                persons = get_object_or_404(Person, name=name)
                serializer = self.serializer_class(persons)
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

    def put(self, request, pk=None, name= None):
        if request.method == 'PUT':

            if pk is not None:
                persons = get_object_or_404(Person, pk=pk)
            elif name is not None:
                persons = get_object_or_404(Person, name=name)
            else:
                return Response(data={'error':'Person instance unavailabled'}, status=status.HTTP_400_BAD_REQUEST)
        
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

    def delete(self, request, pk=None, name =None):
        if pk is not None:
            persons = get_object_or_404(Person, name=name)
        elif name is not None:
            persons = get_object_or_404(Person, name=name)


        persons.delete()
        return Response(data={'message': 'Person instance successfully deleted'}, status=status.HTTP_204_NO_CONTENT)




            



