from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','userId', 'email', 'firstName', 'lastName', 'phone')


admin.site.register(User, UserAdmin)
