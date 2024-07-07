from django.db import models
import uuid
from django.contrib.auth import get_user_model


User = get_user_model()


class Organisation(models.Model):
    orgId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class OrganizationMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='org_memberships')
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='member_orgs')

    def __str__(self):
        return self.user.email + ' - ' + self.organization.name
