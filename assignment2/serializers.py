from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    name =  serializers.CharField(max_length=50)
    bio =  serializers.CharField()

    class Meta:
        model = Person
        fields = ['id','name',  'bio']