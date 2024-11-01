from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Relation, Profile


class EmployeeInline(admin.StackedInline):
    model = Profile
    can_delete = False


# Define a new User admin
class ExtendedUser(UserAdmin):
    inlines = [EmployeeInline]

admin.site.unregister(User)
admin.site.register(User, ExtendedUser)
# Register your models here.
admin.site.register(Relation)
