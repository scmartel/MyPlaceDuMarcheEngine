from django.contrib import admin

# Register your models here.
from .models import User_input, Organization

admin.site.register(User_input)
admin.site.register(Organization)