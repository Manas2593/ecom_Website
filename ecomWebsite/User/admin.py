from django.contrib import admin
from django.contrib.auth import get_user_model
from User.models import regUser, userProfile
# get_user_model
# Register your models here.
regUser = get_user_model()
admin.site.register(regUser)

# Profiles
admin.site.register(userProfile)