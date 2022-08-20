from django.contrib import admin

# Register your models here.

from myusers.models import User

admin.site.register(User)