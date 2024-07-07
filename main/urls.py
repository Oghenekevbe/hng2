from django.urls import path
from .views import UserDetailView, UserOrganisationsView, OrganisationDetailView,  AddUserToOrganisationView

urlpatterns = [
    path('users/<uuid_str>', UserDetailView.as_view(), name='user_detail'),
    path('organisations', UserOrganisationsView.as_view(), name='user_organisations'),
    path('organisations/<uuid_str>', OrganisationDetailView.as_view(), name='organisation_detail'),
    path('organisations/<uuid:orgId>/users', AddUserToOrganisationView.as_view(), name='add_user_to_organisation'),
    
]
