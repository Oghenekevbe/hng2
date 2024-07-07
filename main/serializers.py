from rest_framework import serializers
from .models import Organisation, OrganizationMembership

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['orgId', 'name', 'description']

    def validate_name(self, value):
        # Ensure organisation name is not null or empty
        if not value:
            raise serializers.ValidationError("name cannot be empty.")
        return value

class OrganizationMembershipSerializer(serializers.ModelSerializer):
    orgId = serializers.UUIDField(source='organization.orgId')
    name = serializers.CharField(source='organization.name')
    description = serializers.CharField(source='organization.description')

    class Meta:
        model = OrganizationMembership
        fields = ['orgId', 'name', 'description']