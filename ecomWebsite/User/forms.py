from django.contrib.auth.forms import UserCreationForm
from User.models import regUser

# Create your forms here

class createregUser(UserCreationForm):
    class Meta:
        model = regUser
        fields = ('email',)