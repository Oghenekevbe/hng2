from django.contrib import admin

from .models import  Organisation, OrganizationMembership


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id','orgId', 'name', 'description')

class OrganizationMembershipAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'organization')

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(OrganizationMembership, OrganizationMembershipAdmin)
